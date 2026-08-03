# Alibaba OpenCodeReview

> Pillar: **Advanced Agent Capabilities** · **MCP adapter**

| | |
|---|---|
| **Upstream** | https://github.com/alibaba/open-code-review |
| **License** | `Apache-2.0` |
| **Bus transport** | `adapter` / `stdio` |
| **MCP tools** | `review_diff`, `review_pr`, `review_files` |

## What it does
AI code review combining a deterministic engineering pipeline (file selection, bundling, rule matching, comment positioning) with an LLM agent. Single static Go binary, ~1/9th the tokens of general agents.

## How it plugs in
Adapter shells the `ocr` Go binary and exposes MCP tools `review_diff`, `review_pr`, `review_files`. Also wired as a GitHub Action for CI.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/alibaba/open-code-review), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/opencodereview/config.example.toml integrations/opencodereview/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "opencodereview"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
