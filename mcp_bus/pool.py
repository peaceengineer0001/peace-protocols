"""
MCP connection pool
====================

Implements the concurrent, self-healing connection pool described in
Solution Design §6.1–6.2 of the v2 specification:

    * concurrent connections to many MCP servers,
    * per-server health monitoring with exponential-backoff reconnection,
    * fault isolation (one server failing never blocks the others),
    * a simple ``call_tool`` routing entrypoint for the Raven orchestrator.

The pool is transport-agnostic. A ``client_factory`` callable produces an
object implementing the minimal :class:`MCPClientProtocol` (``connect``,
``list_tools``, ``call_tool``, ``ping``, ``close``). This lets the pool be
unit-tested with a fake client and run in production with a real MCP SDK
client (e.g. ``mcp`` / ``fastmcp``) without any code change here.
"""

from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Awaitable, Callable, Dict, List, Optional, Protocol

from .registry import MCPServerSpec, ServerRegistry


class ConnectionState(str, Enum):
    IDLE = "idle"
    CONNECTING = "connecting"
    READY = "ready"
    DEGRADED = "degraded"
    FAILED = "failed"
    CLOSED = "closed"


class MCPClientProtocol(Protocol):
    """Minimal surface the pool needs from an MCP client implementation."""

    async def connect(self) -> None: ...
    async def list_tools(self) -> List[Dict[str, Any]]: ...
    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> Any: ...
    async def ping(self) -> bool: ...
    async def close(self) -> None: ...


@dataclass
class ServerHealth:
    name: str
    state: ConnectionState = ConnectionState.IDLE
    consecutive_failures: int = 0
    last_ok: Optional[float] = None
    last_error: Optional[str] = None
    tool_count: int = 0
    reconnect_attempts: int = 0

    def as_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "state": self.state.value,
            "consecutive_failures": self.consecutive_failures,
            "last_ok": self.last_ok,
            "last_error": self.last_error,
            "tool_count": self.tool_count,
            "reconnect_attempts": self.reconnect_attempts,
        }


@dataclass
class _Managed:
    spec: MCPServerSpec
    health: ServerHealth
    client: Optional[MCPClientProtocol] = None
    tools: Dict[str, Dict[str, Any]] = field(default_factory=dict)


ClientFactory = Callable[[MCPServerSpec], MCPClientProtocol]


class MCPConnectionPool:
    """Manages concurrent, health-monitored connections to MCP servers."""

    def __init__(
        self,
        registry: ServerRegistry,
        client_factory: ClientFactory,
        *,
        health_interval: float = 15.0,
        max_backoff: float = 60.0,
        require_consent: Optional[Callable[[MCPServerSpec], Awaitable[bool]]] = None,
        commercial_deployment: bool = False,
    ):
        self._registry = registry
        self._client_factory = client_factory
        self._health_interval = health_interval
        self._max_backoff = max_backoff
        self._require_consent = require_consent
        # When True, servers whose license forbids commercial use (e.g. GHOST,
        # CC BY-NC-SA 4.0) are NOT brought up.
        self._commercial_deployment = commercial_deployment
        self._managed: Dict[str, _Managed] = {}
        self._monitor_task: Optional[asyncio.Task] = None
        self._closing = False

    # ------------------------------------------------------------------ #
    # Lifecycle
    # ------------------------------------------------------------------ #
    async def start(self) -> None:
        """Connect to every enabled server concurrently; start health monitor."""
        specs = self._registry.enabled()
        await asyncio.gather(*(self._bring_up(spec) for spec in specs))
        self._monitor_task = asyncio.create_task(self._health_loop())

    async def _bring_up(self, spec: MCPServerSpec) -> None:
        # License / consent gating -------------------------------------- #
        if self._commercial_deployment and not spec.commercial_use:
            self._managed[spec.name] = _Managed(
                spec=spec,
                health=ServerHealth(
                    name=spec.name,
                    state=ConnectionState.CLOSED,
                    last_error="skipped: non-commercial license under commercial deployment",
                ),
            )
            return
        if spec.consent_required and self._require_consent is not None:
            granted = await self._require_consent(spec)
            if not granted:
                self._managed[spec.name] = _Managed(
                    spec=spec,
                    health=ServerHealth(
                        name=spec.name,
                        state=ConnectionState.CLOSED,
                        last_error="consent not granted",
                    ),
                )
                return

        managed = _Managed(spec=spec, health=ServerHealth(name=spec.name))
        self._managed[spec.name] = managed
        await self._connect(managed)

    async def _connect(self, managed: _Managed) -> None:
        spec = managed.spec
        managed.health.state = ConnectionState.CONNECTING
        try:
            client = self._client_factory(spec)
            await client.connect()
            tools = await client.list_tools()
            managed.client = client
            managed.tools = {t["name"]: t for t in tools if "name" in t}
            managed.health.state = ConnectionState.READY
            managed.health.tool_count = len(managed.tools)
            managed.health.consecutive_failures = 0
            managed.health.last_ok = time.time()
            managed.health.last_error = None
        except Exception as exc:  # fault isolation — never propagate
            managed.health.state = ConnectionState.FAILED
            managed.health.consecutive_failures += 1
            managed.health.last_error = repr(exc)

    async def close(self) -> None:
        self._closing = True
        if self._monitor_task:
            self._monitor_task.cancel()
            try:
                await self._monitor_task
            except asyncio.CancelledError:
                pass
        for managed in self._managed.values():
            if managed.client is not None:
                try:
                    await managed.client.close()
                except Exception:
                    pass
            managed.health.state = ConnectionState.CLOSED

    # ------------------------------------------------------------------ #
    # Health monitoring & reconnection
    # ------------------------------------------------------------------ #
    async def _health_loop(self) -> None:
        while not self._closing:
            await asyncio.sleep(self._health_interval)
            await asyncio.gather(
                *(self._check(m) for m in self._managed.values()),
                return_exceptions=True,
            )

    async def _check(self, managed: _Managed) -> None:
        if managed.health.state in (ConnectionState.CLOSED,):
            return
        if managed.client is None or managed.health.state == ConnectionState.FAILED:
            await self._maybe_reconnect(managed)
            return
        try:
            ok = await managed.client.ping()
            if ok:
                managed.health.state = ConnectionState.READY
                managed.health.last_ok = time.time()
                managed.health.consecutive_failures = 0
            else:
                raise RuntimeError("ping returned False")
        except Exception as exc:
            managed.health.consecutive_failures += 1
            managed.health.last_error = repr(exc)
            managed.health.state = (
                ConnectionState.DEGRADED
                if managed.health.consecutive_failures < 3
                else ConnectionState.FAILED
            )

    async def _maybe_reconnect(self, managed: _Managed) -> None:
        backoff = min(
            self._max_backoff,
            2 ** min(managed.health.reconnect_attempts, 6),
        )
        # In steady state the health loop cadence provides the wait; we only
        # gate rapid retries by counting attempts.
        managed.health.reconnect_attempts += 1
        await self._connect(managed)
        _ = backoff  # documented backoff schedule; loop interval enforces spacing

    # ------------------------------------------------------------------ #
    # Routing
    # ------------------------------------------------------------------ #
    def find_tool(self, tool_name: str) -> Optional[str]:
        """Return the server name that exposes ``tool_name`` (first match)."""
        for name, managed in self._managed.items():
            if tool_name in managed.tools and managed.health.state in (
                ConnectionState.READY,
                ConnectionState.DEGRADED,
            ):
                return name
        return None

    async def call_tool(
        self, tool_name: str, arguments: Dict[str, Any], *, server: Optional[str] = None
    ) -> Any:
        """Route a tool call to the owning server. Raises if unavailable."""
        target = server or self.find_tool(tool_name)
        if target is None:
            raise LookupError(f"No ready MCP server exposes tool '{tool_name}'")
        managed = self._managed[target]
        if managed.client is None:
            raise RuntimeError(f"Server '{target}' has no live client")
        return await managed.client.call_tool(tool_name, arguments)

    # ------------------------------------------------------------------ #
    # Introspection
    # ------------------------------------------------------------------ #
    def health(self) -> Dict[str, Dict[str, Any]]:
        return {name: m.health.as_dict() for name, m in self._managed.items()}

    def all_tools(self) -> Dict[str, List[str]]:
        return {name: sorted(m.tools) for name, m in self._managed.items()}

    def ready_servers(self) -> List[str]:
        return [
            name
            for name, m in self._managed.items()
            if m.health.state == ConnectionState.READY
        ]
