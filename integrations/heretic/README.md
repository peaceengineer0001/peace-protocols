# Heretic

> Pillar: **Intelligence & Automation** · **MCP adapter** · **⚠ consent-gated**

| | |
|---|---|
| **Upstream** | https://github.com/p-e-w/heretic |
| **License** | `AGPL-3.0` |
| **Bus transport** | `adapter` / `stdio` |
| **MCP tools** | `estimate_run`, `abliterate_model` |

## What it does
Automatic directional-ablation tool that removes refusal/censorship alignment from HF dense transformers via LoRA adapters + Optuna TPE optimization, co-minimizing refusals and KL divergence. Lets a community align local models to its own values.

## How it plugs in
OFF by default (`enabled: false`) and CONSENT-GATED: the bus requires explicit, logged user consent before any abliteration run. Adapter exposes `abliterate_model`, `estimate_run` only after consent. See CONSENT.md.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/p-e-w/heretic), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/heretic/config.example.toml integrations/heretic/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "heretic"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.

See [`CONSENT.md`](CONSENT.md) before enabling.
