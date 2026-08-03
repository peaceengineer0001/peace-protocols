# LeanCTX

> Pillar: **Advanced Agent Capabilities** · **Native MCP**

| | |
|---|---|
| **Upstream** | https://github.com/yvgude/lean-ctx |
| **License** | `Apache-2.0` |
| **Bus transport** | `native` / `stdio` |
| **MCP tools** | `compress_read`, `route_intent`, `memory_query` |

## What it does
Context-engineering layer (single Rust binary) cutting tokens 60-90% across compression, routing, memory and verification. 10 file-read modes, 95 shell-output patterns, tree-sitter AST for 27 languages, temporal knowledge-graph memory.

## How it plugs in
Ships 82 NATIVE MCP tools (`leanctx mcp`). Sits between Agent Zero and the model backend (AirLLM or cloud), compressing every file read / shell output / payload. Registered directly on the bus.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/yvgude/lean-ctx), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/leanctx/config.example.toml integrations/leanctx/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "leanctx"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
