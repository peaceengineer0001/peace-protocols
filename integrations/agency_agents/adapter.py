"""
MCP adapter for Agency Agents
=============================

Upstream: https://github.com/msitarzewski/agency-agents
License:  MIT
Transport on the Peace Protocols bus: adapter / stdio

This is an INTEGRATION SCAFFOLD. The adapter class and tool list are
production-shaped, but calls require the upstream service (above) to be
installed and running — see this directory's README.md. It is wired into
the Unified MCP Bus via config/mcp_servers.yaml.

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
    {"name": "list_personas", "description": "List available specialist personalities", "inputSchema": {"type": "object"}},
    {"name": "install_persona", "description": "Install a persona as an Agent Zero template", "inputSchema": {"type": "object"}},
    {"name": "invoke_persona", "description": "Invoke a specialist persona", "inputSchema": {"type": "object"}},
]

NATIVE_MCP = False
CONSENT_REQUIRED = False
COMMERCIAL_USE = True


class AgencyAgentsAdapter:
    """Wrap Agency Agents as an MCP server on the Peace Protocols bus."""

    name = "agency-agents"

    def __init__(self, spec: Any = None, **kwargs: Any):
        self.spec = spec
        self.options = kwargs
        self._connected = False

    async def connect(self) -> None:
        # TODO: establish the upstream connection (stdio). Requires the
        # service described in this directory's README to be installed/running.
        self._connected = True

    async def list_tools(self) -> List[Dict[str, Any]]:
        return TOOLS

    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> Any:
        if not self._connected:
            raise RuntimeError("agency-agents: adapter not connected")
        raise NotImplementedError(
            "agency-agents.call_tool('%s') requires the live upstream service. "
            "See integrations/agency_agents/README.md for setup." % name
        )

    async def ping(self) -> bool:
        return self._connected

    async def close(self) -> None:
        self._connected = False


def build(spec: Any = None, **kwargs: Any) -> "AgencyAgentsAdapter":
    """Factory used by the connection pool's ``client_factory``."""
    return AgencyAgentsAdapter(spec, **kwargs)
