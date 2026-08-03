"""
MCP adapter for GHOST OSINT-CRM
===============================

Upstream: https://github.com/elm1nst3r/GHOST-osint-crm
License:  CC-BY-NC-SA-4.0
Transport on the Peace Protocols bus: native / http

This upstream ships a NATIVE MCP server, so this module is a thin
passthrough/registration shim. The bus connects to the native server
directly (see config/mcp_servers.yaml). Requires the upstream service
to be installed/running — see this directory's README.md.

This adapter follows the thin-wrapper contract expected by
``mcp_bus.pool.MCPConnectionPool`` (see ``MCPClientProtocol``): it presents the
upstream service as a set of MCP tools. Where the upstream ships a native MCP
server this module is a no-op passthrough; where it exposes HTTP/REST/CLI/gRPC
it translates those into MCP tool calls.
"""

from __future__ import annotations

from typing import Any, Dict, List


# Tools this adapter advertises to the bus. Wire these to the real upstream
# endpoints once the service in the README is installed and running.
TOOLS: List[Dict[str, Any]] = [
    {"name": "create_investigation", "description": "Create an investigation", "inputSchema": {"type": "object"}},
    {"name": "manage_entity", "description": "Create/link entities", "inputSchema": {"type": "object"}},
    {"name": "generate_report", "description": "Generate a case report", "inputSchema": {"type": "object"}},
]

NATIVE_MCP = True
CONSENT_REQUIRED = False
COMMERCIAL_USE = False


class GhostAdapter:
    """Wrap GHOST OSINT-CRM as an MCP server on the Peace Protocols bus."""

    name = "ghost"

    def __init__(self, spec: Any = None, **kwargs: Any):
        self.spec = spec
        self.options = kwargs
        self._connected = False

    async def connect(self) -> None:
        # TODO: establish the upstream connection (http). Requires the
        # service described in this directory's README to be installed/running.
        self._connected = True

    async def list_tools(self) -> List[Dict[str, Any]]:
        return TOOLS

    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> Any:
        if not self._connected:
            raise RuntimeError("ghost: adapter not connected")
        raise NotImplementedError(
            "ghost.call_tool('%s') requires the live upstream service. "
            "See integrations/ghost/README.md for setup." % name
        )

    async def ping(self) -> bool:
        return self._connected

    async def close(self) -> None:
        self._connected = False


def build(spec: Any = None, **kwargs: Any) -> "GhostAdapter":
    """Factory used by the connection pool's ``client_factory``."""
    return GhostAdapter(spec, **kwargs)
