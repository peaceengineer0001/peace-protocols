# Shopstr

> Pillar: **Community Economy** · **Native MCP** · **GPL-3.0 copyleft**

| | |
|---|---|
| **Upstream** | https://github.com/shopstr-eng/shopstr |
| **License** | `GPL-3.0` |
| **Bus transport** | `native` / `stdio` |
| **MCP tools** | `list_product`, `search_market`, `checkout` |

## What it does
Permissionless Nostr Bitcoin marketplace: Lightning + on-chain + Cashu ecash, 20+ NIPs (NIP-47/57/60/72/85/99). Integrates natively with the existing Buzz/Nostr layer for a community economy.

## How it plugs in
Ships a NATIVE MCP package (`shopstr-mcp`) for marketplace operations. GPL-3.0 (see LICENSE-COMPLIANCE.md). Pairs with LND for Lightning settlement.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/shopstr-eng/shopstr), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/shopstr/config.example.toml integrations/shopstr/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "shopstr"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.

See [`../../docs/LICENSE-COMPLIANCE.md`](../../docs/LICENSE-COMPLIANCE.md) for license obligations.
