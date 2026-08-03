# VoxCPM

> Pillar: **Advanced Agent Capabilities** · **MCP adapter**

| | |
|---|---|
| **Upstream** | https://github.com/OpenBMB/VoxCPM |
| **License** | `Apache-2.0` |
| **Bus transport** | `adapter` / `http` |
| **MCP tools** | `synthesize`, `design_voice`, `clone_voice` |

## What it does
Tokenizer-free high-fidelity TTS (VoxCPM2, 2B params, 30 languages, 48kHz). Three modes: Voice Design (describe a new voice), Controllable Cloning, Ultimate Cloning. ~8GB VRAM; RTF ~0.3 on an RTX 4090.

## How it plugs in
vLLM-Omni OpenAI-compatible endpoint wrapped as MCP tools `synthesize`, `design_voice`, `clone_voice`. Output is watermarked and auth-gated (security model).

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/OpenBMB/VoxCPM), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/voxcpm/config.example.toml integrations/voxcpm/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "voxcpm"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
