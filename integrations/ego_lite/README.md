# Ego-Lite

> Pillar: **Advanced Agent Capabilities** · **MCP adapter**

| | |
|---|---|
| **Upstream** | https://github.com/citrolabs/ego-lite |
| **License** | `MIT` |
| **Bus transport** | `adapter` / `stdio` |
| **MCP tools** | `open_task_space`, `navigate`, `observe`, `act`, `eval_js` |

## What it does
Chromium browser built for human+agent collaboration: agents share the user's browser with isolated Task Spaces but inherit login state/cookies. Agents call 50+ JS helper functions over CDP (up to 2.5x faster than CLI chaining).

## How it plugs in
Adapter wraps the `ego-browser` CLI as a Browser Manager exposing MCP tools `open_task_space`, `navigate`, `observe`, `act`, `eval_js`.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/citrolabs/ego-lite), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/ego_lite/config.example.toml integrations/ego_lite/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "ego-lite"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
