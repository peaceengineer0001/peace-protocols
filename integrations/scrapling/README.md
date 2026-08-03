# Scrapling

> Pillar: **Advanced Agent Capabilities** · **Native MCP**

| | |
|---|---|
| **Upstream** | https://github.com/D4Vinci/Scrapling |
| **License** | `BSD-3-Clause` |
| **Bus transport** | `native` / `stdio` |
| **MCP tools** | `scrape`, `crawl` |

## What it does
Adaptive, self-healing web scraping framework (adaptive parser + stealth fetchers + spider). Relocates moved DOM elements via similarity matching; StealthyFetcher bypasses Cloudflare Turnstile.

## How it plugs in
Ships a NATIVE MCP server (`scrapling mcp serve`) that pre-extracts targeted content before the LLM sees it, cutting tokens. Registered directly on the bus — no adapter code required.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/D4Vinci/Scrapling), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/scrapling/config.example.toml integrations/scrapling/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "scrapling"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
