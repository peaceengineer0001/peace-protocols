# Peace Protocols v2 — Integrations

The v2 upgrade adds 22 upstream capabilities to the Raven Network, all wired to
the Agent Zero capability layer through the **Unified MCP Bus** (`../mcp_bus/`,
registry at [`../config/mcp_servers.yaml`](../config/mcp_servers.yaml)).

> 🚧 **These are integration scaffolds.** Each directory contains a
> production-shaped MCP adapter, config template, requirements, and setup docs.
> The upstream projects are **not vendored** — install/run each per its own
> instructions (linked below). Live tool calls require the upstream service.
> Six upstreams ship **native** MCP servers and are registered directly.

## Architecture

```
 Raven (Chief of Staff)  ──►  Agent Zero capability layer  ──►  Unified MCP Bus
                                                                  │ (connection pool,
                                                                  │  health monitor,
                                                                  │  auto-reconnect)
        ┌───────────────┬───────────────┬───────────────┬────────┴──────────┐
     native MCP     native MCP        adapter          adapter            adapter
     (scrapling,    (worldmonitor,   (airllm,         (osiris,           (lnd,
      leanctx,       ha-mcp,          voxcpm, ...)      trycomp, ...)      shopstr...)
      ghost, shopstr)
```

## The three capability pillars

### Pillar 1 — Massive Local Inference (PRIMARY)
| Integration | License | Transport | Purpose |
|---|---|---|---|
| [AirLLM](airllm/) | Apache-2.0 | adapter/http | **Primary** weight-streaming inference (Kimi K3 on ~3.72GB VRAM) |

### Pillar 2 — Advanced Agent Capabilities
| Integration | License | Transport | Purpose |
|---|---|---|---|
| [Agency Agents](agency_agents/) | MIT | adapter/stdio | Specialist agent personalities → Agent Zero templates |
| [VoxCPM](voxcpm/) | Apache-2.0 | adapter/http | Tokenizer-free high-fidelity TTS |
| [Speech-to-Speech](speech_to_speech/) | Apache-2.0 | adapter/ws | Realtime VAD→STT→LLM→TTS voice pipeline |
| [Scrapling](scrapling/) | BSD-3-Clause | **native**/stdio | Adaptive self-healing web scraping |
| [OpenCodeReview](opencodereview/) | Apache-2.0 | adapter/stdio | Automated code review (Alibaba) |
| [Ego-Lite](ego_lite/) | MIT | adapter/stdio | Shared-session browser automation |
| [LeanCTX](leanctx/) | Apache-2.0 | **native**/stdio | 60–90% token reduction (82 MCP tools) |
| [World Monitor](worldmonitor/) | AGPL-3.0 | **native**/sse | 500+ feeds global intelligence |
| [ha-mcp](ha_mcp/) | MIT | **native**/stdio | Home Assistant (87 tools) |

### Pillar 3 — Intelligence, Media, Design & Commerce (v2.2)
| Integration | License | Transport | Purpose |
|---|---|---|---|
| [OSIRIS](osiris/) | MIT | adapter/http | Palantir-style 14-domain OSINT + RECON |
| [TryComp CRM](trycomp_crm/) | MIT | adapter/http | Agentic-first relationship management |
| [GHOST](ghost/) | **CC BY-NC-SA 4.0** ⚠ | **native**/http | OSINT investigation mgmt (**non-commercial**) |
| [Heretic](heretic/) | AGPL-3.0 ⚠ | adapter/stdio | Model abliteration (**consent-gated, off by default**) |
| [VideoAgent](videoagent/) | MIT | adapter/http | Video understanding/editing/generation |
| [Bananas](bananas/) | MIT | adapter/stdio | P2P multi-cursor screen sharing |
| [HiveTalk SFU](hivetalk_sfu/) | AGPL-3.0 | adapter/http | Nostr-native video conferencing |
| [LongCat-Video](longcat_video/) | MIT | adapter/http | Long-form video generation (13.6B DiT) |
| [CADAM](cadam/) | **GPL-3.0** | adapter/http | Text/image-to-CAD (OpenSCAD/WASM) |
| [img2threejs](img2threejs/) | Apache-2.0 | adapter/stdio | Image → procedural Three.js model |
| [Shopstr](shopstr/) | **GPL-3.0** | **native**/stdio | Nostr Bitcoin marketplace |
| [LND](lnd/) | MIT | adapter/http | Lightning Network daemon (payment rails) |
| [Marketing Agent](marketing_agent/) | Apache-2.0 | adapter/stdio | Fletcher-Method marketing skill pack |

## License notes
See [`../docs/LICENSE-COMPLIANCE.md`](../docs/LICENSE-COMPLIANCE.md). Key gates,
enforced in code by the bus:
- **GHOST** (CC BY-NC-SA 4.0) is skipped under a commercial deployment
  (`--commercial`).
- **Heretic** is `enabled: false` and requires explicit, logged consent.
- **AGPL-3.0** (World Monitor, Heretic, HiveTalk) and **GPL-3.0** (CADAM,
  Shopstr) are integrated across process/MCP boundaries (mere aggregation), so
  the repo stays Apache-2.0.

## Validate
```bash
python3 scripts/validate_mcp_registry.py   # structural + license + adapter checks
python3 -m mcp_bus.serve --once            # bring the bus up, print health, exit
python3 -m pytest tests/                   # bus unit tests
```
