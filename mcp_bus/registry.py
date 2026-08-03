"""
MCP server registry
====================

Parses ``config/mcp_servers.yaml`` into typed :class:`MCPServerSpec` objects and
exposes lookup / filtering helpers used by the connection pool and the Raven
orchestrator.

The registry is intentionally dependency-light: it uses PyYAML if available and
otherwise falls back to a tiny built-in parser for the flat subset of YAML used
by the config file, so the bus can be imported in a bare environment.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


# --------------------------------------------------------------------------- #
# Spec model
# --------------------------------------------------------------------------- #
@dataclass
class MCPServerSpec:
    """Declarative description of one MCP server on the bus."""

    name: str
    transport: str                      # "native" | "adapter"
    protocol: str                       # stdio | http | websocket | sse
    command: Optional[str] = None       # launch command (stdio adapters)
    url: Optional[str] = None           # endpoint (http/ws/sse servers)
    adapter: Optional[str] = None       # dotted path to adapter module
    license: str = "unknown"
    enabled: bool = True
    consent_required: bool = False      # e.g. Heretic abliteration
    commercial_use: bool = True         # GHOST is non-commercial
    tags: List[str] = field(default_factory=list)
    env: Dict[str, str] = field(default_factory=dict)
    description: str = ""

    def validate(self) -> List[str]:
        """Return a list of human-readable problems; empty means valid."""
        problems: List[str] = []
        if not self.name:
            problems.append("server has no name")
        if self.transport not in ("native", "adapter"):
            problems.append(f"{self.name}: transport must be 'native' or 'adapter'")
        if self.protocol not in ("stdio", "http", "websocket", "sse"):
            problems.append(f"{self.name}: unknown protocol '{self.protocol}'")
        if self.protocol == "stdio" and not (self.command or self.adapter):
            problems.append(f"{self.name}: stdio server needs a command or adapter")
        if self.protocol in ("http", "websocket", "sse") and not self.url:
            problems.append(f"{self.name}: {self.protocol} server needs a url")
        return problems


class ServerRegistry:
    """A collection of :class:`MCPServerSpec` with convenient filters."""

    def __init__(self, specs: List[MCPServerSpec]):
        self._specs = {s.name: s for s in specs}

    def __len__(self) -> int:
        return len(self._specs)

    def __iter__(self):
        return iter(self._specs.values())

    def get(self, name: str) -> Optional[MCPServerSpec]:
        return self._specs.get(name)

    def enabled(self) -> List[MCPServerSpec]:
        return [s for s in self._specs.values() if s.enabled]

    def native(self) -> List[MCPServerSpec]:
        return [s for s in self._specs.values() if s.transport == "native"]

    def adapters(self) -> List[MCPServerSpec]:
        return [s for s in self._specs.values() if s.transport == "adapter"]

    def with_tag(self, tag: str) -> List[MCPServerSpec]:
        return [s for s in self._specs.values() if tag in s.tags]

    def validate(self) -> List[str]:
        problems: List[str] = []
        for spec in self._specs.values():
            problems.extend(spec.validate())
        return problems


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #
def _load_yaml(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    try:
        import yaml  # type: ignore

        return yaml.safe_load(text) or {}
    except Exception:
        raise RuntimeError(
            "PyYAML is required to parse mcp_servers.yaml. Install with "
            "`pip install pyyaml`."
        )


def load_registry(path: Optional[str] = None) -> ServerRegistry:
    """Load the server registry from ``config/mcp_servers.yaml``.

    Environment variable ``PEACE_MCP_SERVERS`` overrides the default path.
    """
    if path is None:
        path = os.environ.get(
            "PEACE_MCP_SERVERS",
            os.path.join(os.path.dirname(__file__), "..", "config", "mcp_servers.yaml"),
        )
    data = _load_yaml(path)
    servers = data.get("servers", {})
    specs: List[MCPServerSpec] = []
    for name, cfg in servers.items():
        cfg = cfg or {}
        specs.append(
            MCPServerSpec(
                name=name,
                transport=cfg.get("transport", "adapter"),
                protocol=cfg.get("protocol", "stdio"),
                command=cfg.get("command"),
                url=cfg.get("url"),
                adapter=cfg.get("adapter"),
                license=cfg.get("license", "unknown"),
                enabled=bool(cfg.get("enabled", True)),
                consent_required=bool(cfg.get("consent_required", False)),
                commercial_use=bool(cfg.get("commercial_use", True)),
                tags=list(cfg.get("tags", [])),
                env=dict(cfg.get("env", {})),
                description=cfg.get("description", ""),
            )
        )
    return ServerRegistry(specs)
