# Agency Agents

> Pillar: **Advanced Agent Capabilities** · **MCP adapter**

| | |
|---|---|
| **Upstream** | https://github.com/msitarzewski/agency-agents |
| **License** | `MIT` |
| **Bus transport** | `adapter` / `stdio` |
| **MCP tools** | `list_personas`, `install_persona`, `invoke_persona` |

## What it does
Curated collection of specialist AI personalities (frontend, backend, DevOps, community, content, data...). Their prompt personality files are converted into Agent Zero agent templates so each becomes a callable skill in Raven's orchestration layer.

## How it plugs in
Adapter converts personality files -> Agent Zero templates and exposes `list_personas`, `install_persona`, `invoke_persona` MCP tools.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/msitarzewski/agency-agents), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/agency_agents/config.example.toml integrations/agency_agents/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "agency-agents"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
