# Peace Protocols v2 Upgrade

This document is the implementation companion to the v2 technical
specifications (`Peace_Protocols_System_Upgrade_v2` and
`..._Specification`). It describes **what landed in this branch** and, honestly,
**what still requires out-of-band setup**.

## What v2 adds

1. **Unified MCP Bus** (`mcp_bus/`) — the central v2 architecture. A concurrent,
   self-healing connection pool that connects the Agent Zero capability layer to
   every integration MCP server, with per-server health monitoring, automatic
   reconnection with backoff, and **fault isolation** (one integration failing
   never takes down the bus). Registry is declared in
   [`config/mcp_servers.yaml`](../config/mcp_servers.yaml).

2. **22 integration scaffolds** (`integrations/`) across three pillars —
   massive local inference (AirLLM, **primary** backend), advanced agent
   capabilities (voice, web intelligence, code review, browser, context
   optimization, situational awareness, smart home), and intelligence/media/
   design/commerce (OSINT, CRM, video, 3D/CAD, Nostr Bitcoin commerce).

3. **Multi-OS deployment** — a reference **NixOS "PeaceOS"** distribution
   (`nixos/` flake + modules), a **Windows 11** installer
   (`platforms/windows/install.ps1`), and a **macOS Homebrew tap**
   (`platforms/macos/`).

## Architecture: Buzz substrate + Agent Zero capability layer

v2 does **not** replace the v1 architecture — it layers on top of it. The
existing **Buzz/Nostr** runtime remains the substrate (relay, identity, MCP
runtime, workspace). A new **Agent Zero capability layer** sits between the
client UI and the Buzz relay, adding a Docker-sandboxed Linux desktop, browser
automation, document co-working, and multi-agent delegation — all exposed
through the same MCP interface. The Unified MCP Bus is how that capability layer
reaches the 22 integrations.

```
 Client UI
    │
 Agent Zero capability layer  ── Unified MCP Bus ──►  22 integration MCP servers
    │                                                  (AirLLM primary inference,
 Buzz / Nostr relay (substrate: identity, transport, audit)   voice, web, intel…)
```

Inference routing: **AirLLM is the primary backend**; cloud APIs are fallback
only, preserving data sovereignty (spec Goal G1). Context passes through LeanCTX
for 60–90% token reduction before reaching any model.

## Data flow (typical interaction)

1. Input arrives as text (Nostr/Buzz), voice (Speech-to-Speech WebSocket), or
   browser (Ego-Lite shared session).
2. Voice input passes VAD/STT; Raven determines intent and selects tools.
3. Raven may query LeanCTX (context), Scrapling (web), World Monitor/OSIRIS
   (intel), or ha-mcp (smart home) over the bus.
4. Inference routes through AirLLM to a local model.
5. TTS output goes to VoxCPM / the Speech-to-Speech TTS stage.
6. Code changes are reviewed by OpenCodeReview before commit.
7. The interaction is logged to Nostr for auditability (kinds `30106` audit,
   `30110` email).

## New Nostr event kinds (v2)
| Kind | Purpose |
|---|---|
| `30106` | Audit log events (incl. Heretic consent) |
| `30110` | Email bridge (OpenShip / nostr-mail) |

## Security model (summary)
See spec §7. Controls implemented/declared: SHA-256 model-weight verification,
Docker-sandboxed browsing (Scrapling/Ego-Lite), ha-mcp read-only mode, local-
first inference, VoxCPM output watermarking + auth gating, Agent Zero sandbox
for tool execution, NIP-59 gift-wrapped agent comms, and pinned dependencies
via NixOS. GHOST non-commercial and Heretic consent gates are enforced in the
bus (`mcp_bus/pool.py`).

## Multi-OS parity matrix
NixOS is the reference platform; Windows 11 and macOS are parity targets. The
full per-component matrix is in the spec (§5) and mirrored in the platform
READMEs (`platforms/windows/README.md`, `platforms/macos/README.md`).

## Honest status

| Area | Status |
|---|---|
| Unified MCP Bus (pool, registry, health, gating, routing) | ✅ Implemented + unit-tested (8/8) |
| `config/mcp_servers.yaml` (23 servers) | ✅ Complete, validated |
| 22 integration adapters + config + docs | 🧩 Scaffolds — adapter contract in place; live calls need upstream services |
| 6 native-MCP registrations | 🧩 Registered; need upstream server installed/running |
| NixOS flake + 6 modules | 🧩 Declarative config authored; not built here (no Nix in CI) |
| Windows installer / macOS tap | 🧩 Authored; not executed here |
| Tests + registry validator | ✅ Passing |

**Why scaffolds?** Fully running all 22 services (multi-GPU video models, an LND
Lightning node, OSIRIS/GHOST Docker stacks, Home Assistant, etc.) requires real
hardware, GPUs, API keys, and external services that cannot be provisioned
inside this build. The deliverable is therefore a production-shaped, tested
integration **framework** plus honest per-integration setup docs — not a claim
that every upstream is live.

## Try it
```bash
pip install pyyaml pytest
python3 scripts/validate_mcp_registry.py
python3 -m mcp_bus.serve --once
python3 -m pytest tests/ -v
```
