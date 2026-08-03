# HiveTalk SFU

> Pillar: **Media Production** · **MCP adapter**

| | |
|---|---|
| **Upstream** | https://github.com/HiveTalk/hivetalksfu |
| **License** | `AGPL-3.0` |
| **Bus transport** | `adapter` / `http` |
| **MCP tools** | `create_room`, `schedule_meeting`, `end_room` |

## What it does
Nostr-native WebRTC video conferencing (fork of MiroTalk SFU) with mediasoup 3.14 SFU, up to 4K, PWA, 133 languages, Lightning micropayments. A user's Nostr identity is both their messaging AND conferencing identity.

## How it plugs in
Adapter wraps the REST API as MCP tools `create_room`, `schedule_meeting`, `end_room`. AGPL-3.0 copyleft.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/HiveTalk/hivetalksfu), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/hivetalk_sfu/config.example.toml integrations/hivetalk_sfu/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "hivetalk-sfu"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
