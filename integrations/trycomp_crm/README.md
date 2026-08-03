# TryComp AI CRM

> Pillar: **Intelligence & Automation** · **MCP adapter**

| | |
|---|---|
| **Upstream** | https://github.com/trycompai/crm |
| **License** | `MIT` |
| **Bus transport** | `adapter` / `http` |
| **MCP tools** | `research_contact`, `enrich_company`, `record_fact`, `schedule_followup` |

## What it does
Agentic-first CRM where a durable research agent (Vercel eve framework) is the product and the DB is just where it writes observed facts. 18 tools (contact research, enrichment, attendee ID, follow-ups). Deny-all-egress sandbox; zero-guessing evidence policy.

## How it plugs in
Turborepo/Bun monorepo (agent + Next.js + NestJS/tRPC + Prisma/Postgres). Adapter wraps the tRPC/REST surface as MCP tools `research_contact`, `enrich_company`, `schedule_followup`, `record_fact`.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/trycompai/crm), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/trycomp_crm/config.example.toml integrations/trycomp_crm/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "trycomp-crm"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
