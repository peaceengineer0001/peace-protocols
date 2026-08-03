# OSIRIS

> Pillar: **Intelligence & Automation** · **MCP adapter**

| | |
|---|---|
| **Upstream** | https://github.com/simplifaisoul/osiris |
| **License** | `MIT` |
| **Bus transport** | `adapter` / `http` |
| **MCP tools** | `query_domain`, `recon`, `sanctions_search` |

## What it does
Open-source Palantir-style intelligence dashboard aggregating 14 live domains (aviation, maritime, CCTV, seismic, wildfire, news, weather, space, cyber/CVE, conflict zones, crypto/OFAC, Telegram OSINT) on a GPU map. Ships a 14+ tool RECON toolkit with SSRF protection.

## How it plugs in
Deploys as 3 Docker services (Next.js app + nginx + Express intel engine). Adapter wraps its REST routes as MCP tools `query_domain`, `recon`, `entity_resolve`, `sanctions_search`.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/simplifaisoul/osiris), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/osiris/config.example.toml integrations/osiris/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "osiris"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
