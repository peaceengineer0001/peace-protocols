# Marketing Agent Framework

> Pillar: **Community Economy** · **MCP adapter**

| | |
|---|---|
| **Upstream** | https://fletchermethod.com |
| **License** | `Apache-2.0` |
| **Bus transport** | `adapter` / `stdio` |
| **MCP tools** | `build_campaign`, `generate_content`, `plan_distribution` |

## What it does
Encodes the Fletcher Method AI marketing strategy (personas -> value props -> channels -> compounding content systems) as Agent Zero skills. Marketing agents run 24/7: outreach, education about Peace Protocols, Nostr community engagement, multimedia production.

## How it plugs in
Skill pack (not a third-party server). Adapter exposes MCP tools `build_campaign`, `generate_content`, `plan_distribution` that orchestrate CRM + OSINT + media + Nostr tools.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://fletchermethod.com), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/marketing_agent/config.example.toml integrations/marketing_agent/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "marketing-agent"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
