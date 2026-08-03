# World Monitor

> Pillar: **Advanced Agent Capabilities** · **Native MCP**

| | |
|---|---|
| **Upstream** | https://github.com/koala73/worldmonitor |
| **License** | `AGPL-3.0` |
| **Bus transport** | `native` / `sse` |
| **MCP tools** | `query_feeds`, `brief` |

## What it does
Real-time global intelligence dashboard: 500+ curated news feeds, 65+ upstream providers, dual 3D/flat map engine, on-device ONNX/Transformers.js news synthesis. AGPL-3.0 (copyleft; compatible with our open-source mission).

## How it plugs in
Hosted NATIVE MCP endpoint at worldmonitor.app/mcp (SSE). Registered directly; agents query global intel programmatically. Self-host option available.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/koala73/worldmonitor), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/worldmonitor/config.example.toml integrations/worldmonitor/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "worldmonitor"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
