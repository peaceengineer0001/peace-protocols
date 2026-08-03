# GHOST OSINT-CRM

> Pillar: **Intelligence & Automation** · **Native MCP** · **⚠ non-commercial license**

| | |
|---|---|
| **Upstream** | https://github.com/elm1nst3r/GHOST-osint-crm |
| **License** | `CC-BY-NC-SA-4.0` |
| **Bus transport** | `native` / `http` |
| **MCP tools** | `create_investigation`, `manage_entity`, `generate_report` |

## What it does
Self-hosted OSINT investigation management: structured case management, ReactFlow entity network graphs, geocoded intel map with WiGLE overlays, asset/property chain-of-custody. React 18 + Express 5 (19 routes, OpenAPI 3.1) + Postgres 15.

## How it plugs in
Ships a NATIVE MCP server auto-generating ~86 tools from its live OpenAPI spec. LICENSE IS CC BY-NC-SA 4.0 (NON-COMMERCIAL): the bus skips GHOST under any commercial deployment. See LICENSE-COMPLIANCE.md.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/elm1nst3r/GHOST-osint-crm), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/ghost/config.example.toml integrations/ghost/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "ghost"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.

See [`../../docs/LICENSE-COMPLIANCE.md`](../../docs/LICENSE-COMPLIANCE.md) for license obligations.
