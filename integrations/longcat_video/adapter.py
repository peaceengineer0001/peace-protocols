"""
MCP adapter for LongCat-Video
=============================

Upstream: https://github.com/meituan-longcat/LongCat-Video
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
    {"name": "text_to_video", "description": "Generate video from text", "inputSchema": {"type": "object"}},
    {"name": "image_to_video", "description": "Animate an image", "inputSchema": {"type": "object"}},
    {"name": "continue_video", "description": "Continue a video", "inputSchema": {"type": "object"}},
    {"name": "avatar", "description": "Audio-driven avatar", "inputSchema": {"type": "object"}},
]

NATIVE_MCP = False
CONSENT_REQUIRED = False
COMMERCIAL_USE = True


class LongcatVideoAdapter:
    """Wrap LongCat-Video as an MCP server on the Peace Protocols bus."""

    name = "longcat-video"

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
            raise RuntimeError("longcat-video: adapter not connected")
        raise NotImplementedError(
            "longcat-video.call_tool('%s') requires the live upstream service. "
            "See integrations/longcat_video/README.md for setup." % name
        )

    async def ping(self) -> bool:
        return self._connected

    async def close(self) -> None:
        self._connected = False


def build(spec: Any = None, **kwargs: Any) -> "LongcatVideoAdapter":
    """Factory used by the connection pool's ``client_factory``."""
    return LongcatVideoAdapter(spec, **kwargs)
