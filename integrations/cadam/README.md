# CADAM

> Pillar: **Design & Fabrication** · **MCP adapter** · **GPL-3.0 copyleft**

| | |
|---|---|
| **Upstream** | https://github.com/Adam-CAD/CADAM |
| **License** | `GPL-3.0` |
| **Bus transport** | `adapter` / `http` |
| **MCP tools** | `text_to_cad`, `image_to_cad`, `export_model` |

## What it does
Text/image-to-CAD web app generating real OpenSCAD code with parametric sliders, Three.js preview, export to STL/SCAD/DXF. OpenSCAD compiled to WASM runs entirely client-side. GPL-3.0.

## How it plugs in
Adapter wraps the generation service as MCP tools `text_to_cad`, `image_to_cad`, `export_model`. See LICENSE-COMPLIANCE.md for GPL-3.0 obligations.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/Adam-CAD/CADAM), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/cadam/config.example.toml integrations/cadam/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "cadam"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.

See [`../../docs/LICENSE-COMPLIANCE.md`](../../docs/LICENSE-COMPLIANCE.md) for license obligations.
