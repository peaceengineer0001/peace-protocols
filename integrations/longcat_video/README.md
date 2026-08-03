# LongCat-Video

> Pillar: **Media Production** · **MCP adapter**

| | |
|---|---|
| **Upstream** | https://github.com/meituan-longcat/LongCat-Video |
| **License** | `MIT` |
| **Bus transport** | `adapter` / `http` |
| **MCP tools** | `text_to_video`, `image_to_video`, `continue_video`, `avatar` |

## What it does
13.6B-param Diffusion-Transformer video model (Meituan): text/image-to-video and video continuation, minutes-long output without drift, 720p@30fps, audio-driven avatars. Single/multi-GPU via torchrun + context parallelism.

## How it plugs in
Adapter wraps inference as MCP tools `text_to_video`, `image_to_video`, `continue_video`, `avatar`. GPU-heavy; queue-backed.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/meituan-longcat/LongCat-Video), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/longcat_video/config.example.toml integrations/longcat_video/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "longcat-video"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
