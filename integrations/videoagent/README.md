# VideoAgent

> Pillar: **Media Production** · **MCP adapter**

| | |
|---|---|
| **Upstream** | https://github.com/HKUDS/VideoAgent |
| **License** | `MIT` |
| **Bus transport** | `adapter` / `http` |
| **MCP tools** | `analyze_video`, `edit_video`, `remake_video` |

## What it does
All-in-one agentic framework for video understanding, editing and generation (HKU Data Science Lab). Intent analysis -> graph workflow -> multi-modal storyboard. Bundles Faster-Whisper, Demucs, CosyVoice, Seed-VC, DiffSinger.

## How it plugs in
Adapter wraps its service as MCP tools `analyze_video`, `edit_video`, `remake_video`.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/HKUDS/VideoAgent), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/videoagent/config.example.toml integrations/videoagent/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "videoagent"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
