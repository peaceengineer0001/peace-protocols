# AirLLM

> Pillar: **Massive Local Inference** · **MCP adapter** · **PRIMARY inference backend**

| | |
|---|---|
| **Upstream** | https://github.com/lyogavin/airllm |
| **License** | `Apache-2.0` |
| **Bus transport** | `adapter` / `http` |
| **MCP tools** | `infer`, `embed`, `list_models` |

## What it does
Weight/expert-streaming inference engine. Runs frontier models (Kimi K3 2.8T MoE) on consumer GPUs (~3.72GB VRAM) by streaming one layer/expert at a time from disk to GPU with a background prefetch thread. This is the PRIMARY inference backend for every Peace Protocols agent; cloud APIs are fallback only.

## How it plugs in
Exposes an OpenAI-compatible /v1 endpoint (chat/completions, embeddings) that the adapter surfaces as MCP tools `infer`, `embed`, `list_models`.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/lyogavin/airllm), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/airllm/config.example.toml integrations/airllm/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "airllm"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
