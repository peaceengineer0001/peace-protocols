# LND (Lightning Network Daemon)

> Pillar: **Community Economy** · **MCP adapter**

| | |
|---|---|
| **Upstream** | https://github.com/lightningnetwork/lnd |
| **License** | `MIT` |
| **Bus transport** | `adapter` / `http` |
| **MCP tools** | `create_invoice`, `pay_invoice`, `channel_balance`, `open_channel` |

## What it does
Production Lightning node (full BOLT compliance, btcd/Bitcoin Core/Neutrino backends, gRPC+REST). Provides the payment rails Shopstr, HiveTalk and the community treasury settle on. Nostr keys are natively Taproot-compatible (one keypair for comms + value).

## How it plugs in
Adapter wraps LND REST (macaroon + TLS cert auth) as MCP tools `create_invoice`, `pay_invoice`, `channel_balance`, `open_channel`.

## Setup (out-of-band)
The upstream project is **not vendored** into this repo. Install/run it per its
own instructions (https://github.com/lightningnetwork/lnd), copy `config.example.toml` → `config.toml`, then
enable it in [`config/mcp_servers.yaml`](../../config/mcp_servers.yaml). The
Unified MCP Bus (`mcp_bus/`) will connect on startup with health monitoring and
automatic reconnection.

```bash
# 1. install upstream (see its README)
# 2. configure this adapter
cp integrations/lnd/config.example.toml integrations/lnd/config.toml
# 3. it is already registered in config/mcp_servers.yaml as "lnd"
```

## Status
🚧 **Integration scaffold.** Adapter contract, tool surface, config and bus
registration are in place. Live tool calls require the upstream service above to
be installed and running.
