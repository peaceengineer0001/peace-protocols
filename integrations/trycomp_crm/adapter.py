"""
MCP adapter for TryComp AI CRM
==============================

Upstream: https://github.com/trycompai/crm
License:  MIT
Transport on the Peace Protocols bus: adapter / http

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
    {"name": "research_contact", "description": "Research a contact", "inputSchema": {"type": "object"}},
    {"name": "enrich_company", "description": "Enrich a company", "inputSchema": {"type": "object"}},
    {"name": "record_fact", "description": "Record an observed fact", "inputSchema": {"type": "object"}},
    {"name": "schedule_followup", "description": "Schedule a follow-up", "inputSchema": {"type": "object"}},
]

NATIVE_MCP = False
CONSENT_REQUIRED = False
COMMERCIAL_USE = True


class TrycompCrmAdapter:
    """Wrap TryComp AI CRM as an MCP server on the Peace Protocols bus."""

    name = "trycomp-crm"

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
            raise RuntimeError("trycomp-crm: adapter not connected")
        raise NotImplementedError(
            "trycomp-crm.call_tool('%s') requires the live upstream service. "
            "See integrations/trycomp_crm/README.md for setup." % name
        )

    async def ping(self) -> bool:
        return self._connected

    async def close(self) -> None:
        self._connected = False


def build(spec: Any = None, **kwargs: Any) -> "TrycompCrmAdapter":
    """Factory used by the connection pool's ``client_factory``."""
    return TrycompCrmAdapter(spec, **kwargs)
