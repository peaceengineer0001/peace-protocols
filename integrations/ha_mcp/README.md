# Home Assistant MCP (ha-mcp)

> Pillar: **Advanced Agent Capabilities** · **Native MCP**

| | |
|---|---|
| **Upstream** | https://github.com/homeassistant-ai/ha-mcp |
| **License** | `MIT` |
| **Bus transport** | `native` / `stdio` |
| **MCP tools** | `search_entities`, `control_device`, `create_automation` |

## What it does
Exposes the full Home Assistant surface via 87 tools across search, device control, config, monitoring, admin and safety. FastMCP + Python 3.13, lazy init. Read-Only Mode with per-tool enable/disable for safety.

## How it plugs in
NATIVE MCP server (`ha-mcp serve`). Needs HOME_ASSISTANT_URL + long-lived token in env. Registered directly on the bus.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/homeassistant-ai/ha-mcp), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/ha_mcp/config.example.toml integrations/ha_mcp/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "ha-mcp"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
