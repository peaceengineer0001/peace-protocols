"""
Tests for the Unified MCP Bus (mcp_bus/): registry parsing, connection pool
lifecycle, fault isolation, license/consent gating, and tool routing.

Run:  python3 -m pytest tests/ -v      (or: python3 tests/test_mcp_bus.py)
"""

from __future__ import annotations

import asyncio
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from mcp_bus.registry import load_registry, MCPServerSpec, ServerRegistry
from mcp_bus.pool import MCPConnectionPool, ConnectionState


# --------------------------------------------------------------------------- #
# Fakes
# --------------------------------------------------------------------------- #
class FakeClient:
    """In-memory MCP client for tests."""

    def __init__(self, spec, *, tools=None, fail_connect=False, fail_ping=False):
        self.spec = spec
        self._tools = tools or [{"name": f"{spec.name}.tool"}]
        self._fail_connect = fail_connect
        self._fail_ping = fail_ping
        self.connected = False
        self.calls = []

    async def connect(self):
        if self._fail_connect:
            raise RuntimeError("boom")
        self.connected = True

    async def list_tools(self):
        return self._tools

    async def call_tool(self, name, arguments):
        self.calls.append((name, arguments))
        return {"ok": True, "server": self.spec.name, "tool": name}

    async def ping(self):
        return not self._fail_ping

    async def close(self):
        self.connected = False


def _registry(*specs):
    return ServerRegistry(list(specs))


# --------------------------------------------------------------------------- #
# Registry
# --------------------------------------------------------------------------- #
def test_real_registry_loads_and_validates():
    reg = load_registry()
    assert len(reg) >= 22, "expected all v2 integrations registered"
    assert reg.validate() == [], "registry should have no structural problems"
    # AirLLM is the primary inference backend and must be present + enabled.
    air = reg.get("airllm")
    assert air is not None and air.enabled
    # GHOST must be flagged non-commercial.
    ghost = reg.get("ghost")
    assert ghost is not None and ghost.commercial_use is False
    # Heretic must be disabled by default and consent-gated.
    heretic = reg.get("heretic")
    assert heretic is not None and heretic.enabled is False and heretic.consent_required


def test_spec_validation_flags_bad_specs():
    bad = MCPServerSpec(name="x", transport="native", protocol="http")  # http needs url
    problems = bad.validate()
    assert any("url" in p for p in problems)


# --------------------------------------------------------------------------- #
# Pool lifecycle & routing
# --------------------------------------------------------------------------- #
def test_pool_brings_up_all_servers():
    async def run():
        reg = _registry(
            MCPServerSpec(name="a", transport="adapter", protocol="stdio", adapter="x"),
            MCPServerSpec(name="b", transport="adapter", protocol="stdio", adapter="x"),
        )
        pool = MCPConnectionPool(reg, client_factory=lambda s: FakeClient(s))
        await pool.start()
        assert set(pool.ready_servers()) == {"a", "b"}
        await pool.close()
    asyncio.run(run())


def test_fault_isolation_one_failure_does_not_block_others():
    async def run():
        reg = _registry(
            MCPServerSpec(name="good", transport="adapter", protocol="stdio", adapter="x"),
            MCPServerSpec(name="bad", transport="adapter", protocol="stdio", adapter="x"),
        )

        def factory(spec):
            return FakeClient(spec, fail_connect=(spec.name == "bad"))

        pool = MCPConnectionPool(reg, client_factory=factory)
        await pool.start()
        health = pool.health()
        assert health["good"]["state"] == ConnectionState.READY.value
        assert health["bad"]["state"] == ConnectionState.FAILED.value
        assert pool.ready_servers() == ["good"]
        await pool.close()
    asyncio.run(run())


def test_tool_routing_and_call():
    async def run():
        reg = _registry(
            MCPServerSpec(name="s1", transport="adapter", protocol="stdio", adapter="x"),
        )
        pool = MCPConnectionPool(
            reg, client_factory=lambda s: FakeClient(s, tools=[{"name": "do_thing"}])
        )
        await pool.start()
        assert pool.find_tool("do_thing") == "s1"
        result = await pool.call_tool("do_thing", {"k": 1})
        assert result["ok"] and result["tool"] == "do_thing"
        # Unknown tool raises.
        try:
            await pool.call_tool("nope", {})
            assert False, "expected LookupError"
        except LookupError:
            pass
        await pool.close()
    asyncio.run(run())


# --------------------------------------------------------------------------- #
# License & consent gating
# --------------------------------------------------------------------------- #
def test_non_commercial_server_skipped_under_commercial_deployment():
    async def run():
        reg = _registry(
            MCPServerSpec(name="ghost", transport="adapter", protocol="stdio",
                          adapter="x", commercial_use=False),
            MCPServerSpec(name="ok", transport="adapter", protocol="stdio", adapter="x"),
        )
        pool = MCPConnectionPool(
            reg, client_factory=lambda s: FakeClient(s), commercial_deployment=True
        )
        await pool.start()
        assert pool.health()["ghost"]["state"] == ConnectionState.CLOSED.value
        assert "ghost" not in pool.ready_servers()
        assert "ok" in pool.ready_servers()
        await pool.close()
    asyncio.run(run())


def test_non_commercial_server_runs_under_non_commercial_deployment():
    async def run():
        reg = _registry(
            MCPServerSpec(name="ghost", transport="adapter", protocol="stdio",
                          adapter="x", commercial_use=False),
        )
        pool = MCPConnectionPool(
            reg, client_factory=lambda s: FakeClient(s), commercial_deployment=False
        )
        await pool.start()
        assert "ghost" in pool.ready_servers()
        await pool.close()
    asyncio.run(run())


def test_consent_gated_server_requires_consent():
    async def run():
        reg = _registry(
            MCPServerSpec(name="heretic", transport="adapter", protocol="stdio",
                          adapter="x", consent_required=True),
        )

        async def deny(spec):
            return False

        pool = MCPConnectionPool(reg, client_factory=lambda s: FakeClient(s),
                                 require_consent=deny)
        await pool.start()
        assert "heretic" not in pool.ready_servers()
        assert pool.health()["heretic"]["state"] == ConnectionState.CLOSED.value
        await pool.close()

        # Now grant consent.
        async def grant(spec):
            return True

        pool2 = MCPConnectionPool(reg, client_factory=lambda s: FakeClient(s),
                                  require_consent=grant)
        await pool2.start()
        assert "heretic" in pool2.ready_servers()
        await pool2.close()
    asyncio.run(run())


# --------------------------------------------------------------------------- #
# Manual runner (no pytest dependency required)
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    passed = 0
    for fn in fns:
        fn()
        print(f"PASS {fn.__name__}")
        passed += 1
    print(f"\n{passed}/{len(fns)} tests passed")
