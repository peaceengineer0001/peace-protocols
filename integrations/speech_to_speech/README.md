# HuggingFace Speech-to-Speech

> Pillar: **Advanced Agent Capabilities** · **MCP adapter**

| | |
|---|---|
| **Upstream** | https://github.com/huggingface/speech-to-speech |
| **License** | `Apache-2.0` |
| **Bus transport** | `adapter` / `websocket` |
| **MCP tools** | `start_session`, `push_audio`, `stop_session` |

## What it does
Low-latency cascade voice pipeline VAD -> STT -> LLM -> TTS with an OpenAI Realtime-compatible WebSocket API. STT defaults to Parakeet TDT; LLM stage connects to the AirLLM backend; TTS stage routes to VoxCPM.

## How it plugs in
Adapter manages the Realtime WebSocket and exposes MCP tools `start_session`, `push_audio`, `stop_session` plus a Voice Manager hook for Agent Zero.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/huggingface/speech-to-speech), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/speech_to_speech/config.example.toml integrations/speech_to_speech/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "speech-to-speech"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
