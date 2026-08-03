"""
``python -m mcp_bus.serve`` — bring up the Unified MCP Bus.

This is the process the NixOS module, the Windows installer, and the Homebrew
formula all launch. It loads ``config/mcp_servers.yaml``, constructs the
connection pool, and runs the health-monitoring loop until interrupted.

A real MCP client is injected via ``client_factory``. In this scaffold the
factory returns each integration's adapter (``integrations.<name>.adapter``)
for stdio/adapter servers, and a light HTTP/WS/SSE client stub for native
servers. Wire these to a production MCP SDK client (e.g. ``mcp``/``fastmcp``)
when deploying.
"""

from __future__ import annotations

import argparse
import asyncio
import importlib
import logging
import os
from typing import Any

from .registry import MCPServerSpec, load_registry
from .pool import MCPConnectionPool

log = logging.getLogger("peace.mcp_bus")


def _adapter_client(spec: MCPServerSpec) -> Any:
    """Instantiate an integration adapter as the MCP client for a spec."""
    module_path = spec.adapter
    if not module_path:
        # Native servers without an adapter module use a generic client stub.
        return _NativeClientStub(spec)
    mod = importlib.import_module(module_path)
    if hasattr(mod, "build"):
        return mod.build(spec)
    # Fall back to the first *Adapter class in the module.
    for attr in dir(mod):
        if attr.endswith("Adapter"):
            return getattr(mod, attr)(spec)
    raise RuntimeError(f"{module_path}: no build()/*Adapter found")


class _NativeClientStub:
    """Placeholder client for native MCP servers.

    Replace with a real MCP SDK transport client (stdio/http/ws/sse) at deploy
    time. It advertises no tools until connected to the live server.
    """

    def __init__(self, spec: MCPServerSpec):
        self.spec = spec
        self._connected = False

    async def connect(self) -> None:
        # A production build launches spec.command (stdio) or dials spec.url.
        self._connected = True

    async def list_tools(self):
        return []

    async def call_tool(self, name: str, arguments: dict) -> Any:
        raise NotImplementedError(
            f"{self.spec.name}: native MCP server not attached in scaffold mode"
        )

    async def ping(self) -> bool:
        return self._connected

    async def close(self) -> None:
        self._connected = False


async def _consent(spec: MCPServerSpec) -> bool:
    """Consent gate for consent_required servers (e.g. Heretic)."""
    env_flag = os.environ.get(f"PEACE_CONSENT_{spec.name.upper().replace('-', '_')}")
    return env_flag == "1"


async def main_async(args: argparse.Namespace) -> None:
    registry = load_registry(args.config)
    problems = registry.validate()
    if problems:
        for p in problems:
            log.error("registry: %s", p)
        raise SystemExit(2)

    pool = MCPConnectionPool(
        registry,
        client_factory=_adapter_client,
        require_consent=_consent,
        commercial_deployment=args.commercial,
    )
    await pool.start()

    log.info("MCP bus up. Ready servers: %s", ", ".join(pool.ready_servers()) or "(none attached)")
    log.info("Registered: %d servers (%d native, %d adapters)",
             len(registry), len(registry.native()), len(registry.adapters()))

    if args.once:
        log.info("health: %s", pool.health())
        await pool.close()
        return

    try:
        while True:
            await asyncio.sleep(args.health_interval)
            ready = pool.ready_servers()
            log.info("heartbeat — %d ready", len(ready))
    except (KeyboardInterrupt, asyncio.CancelledError):
        pass
    finally:
        await pool.close()


def main() -> None:
    ap = argparse.ArgumentParser(description="Peace Protocols Unified MCP Bus")
    ap.add_argument("--config", default=None, help="path to mcp_servers.yaml")
    ap.add_argument("--health-interval", type=float, default=15.0)
    ap.add_argument("--commercial", action="store_true",
                    help="mark this a COMMERCIAL deployment; disables non-commercial-only "
                         "servers such as GHOST (CC BY-NC-SA 4.0)")
    ap.add_argument("--once", action="store_true", help="start, print health, exit (smoke test)")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
