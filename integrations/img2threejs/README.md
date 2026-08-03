# img2threejs

> Pillar: **Design & Fabrication** · **MCP adapter**

| | |
|---|---|
| **Upstream** | https://github.com/img2threejs/img2threejs |
| **License** | `Apache-2.0` |
| **Bus transport** | `adapter` / `stdio` |
| **MCP tools** | `reconstruct`, `refine_pass`, `export_ts` |

## What it does
Agent skill that reconstructs objects from reference images as code-only procedural Three.js/TypeScript models through an 8-pass staged sculpting pipeline with per-pass quality gates and CIEDE2000 color math. Output is animation-ready.

## How it plugs in
Adapter drives the staged pipeline and exposes MCP tools `reconstruct`, `refine_pass`, `export_ts`.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/img2threejs/img2threejs), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/img2threejs/config.example.toml integrations/img2threejs/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "img2threejs"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
