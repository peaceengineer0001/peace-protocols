# Bananas

> Pillar: **Media Production** · **MCP adapter**

| | |
|---|---|
| **Upstream** | https://github.com/mistweaverco/bananas |
| **License** | `MIT` |
| **Bus transport** | `adapter` / `stdio` |
| **MCP tools** | `start_share`, `join_share`, `stop_share` |

## What it does
Cross-platform P2P screen sharing (Electron 31 + Svelte 4 + WebRTC) with multi-cursor collaboration — no accounts, no server (STUN/TURN only). Enables human+agent pair sessions with shared visual context.

## How it plugs in
Adapter launches/controls the Bananas app and exposes MCP tools `start_share`, `join_share`, `stop_share`.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/mistweaverco/bananas), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/bananas/config.example.toml integrations/bananas/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "bananas"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
