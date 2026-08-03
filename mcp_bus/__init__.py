"""
Peace Protocols — Unified MCP Bus
=================================

The Unified MCP Bus is the v2 communication backbone that connects the Agent
Zero capability layer (and, through it, the Raven orchestrator running on the
Buzz/Nostr substrate) to every v2 integration.

Architecture: hub-and-spoke.
    * The Agent Zero fork is the central **MCP client**.
    * Each integration is an independent **MCP server** — either speaking MCP
      natively (Scrapling, LeanCTX, World Monitor, ha-mcp, GHOST, Shopstr) or
      wrapped by a lightweight adapter in ``integrations/<name>/adapter.py``.
    * The :class:`MCPConnectionPool` manages concurrent connections with
      automatic reconnection and health monitoring so that a failure in one
      integration is contained and never takes down the bus.

This package is transport-agnostic: it models the connection lifecycle,
health, routing and registry. The actual MCP wire protocol client is injected
(see ``client_factory`` in :class:`MCPConnectionPool`) so the bus can be
exercised in tests without a live MCP runtime.
"""

from .registry import MCPServerSpec, ServerRegistry, load_registry
from .pool import MCPConnectionPool, ConnectionState, ServerHealth

__all__ = [
    "MCPServerSpec",
    "ServerRegistry",
    "load_registry",
    "MCPConnectionPool",
    "ConnectionState",
    "ServerHealth",
]

__version__ = "2.0.0"
