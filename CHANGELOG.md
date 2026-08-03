# Changelog

All notable changes to **Peace Protocols** are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] — 2026-08-02

The **v2 upgrade** turns the Peace Protocols Buzz overlay into a full **Agent Zero
capability layer** wired through a **Unified MCP Bus**, integrating 22 upstream
services behind one registry-driven, license-aware routing surface.

### Added

#### Unified MCP Bus (`mcp_bus/`)
- Registry-driven bus (`config/mcp_servers.yaml`) declaring **23 MCP servers**
  (native + adapter transports) parsed into typed `MCPServerSpec` objects
  (`mcp_bus/registry.py`).
- Async `MCPConnectionPool` (`mcp_bus/pool.py`) with concurrent startup, per-server
  health monitoring, exponential-backoff reconnection, and fault isolation.
- Serve entrypoint (`mcp_bus/serve.py`, console script `peace-mcp-bus`) to bring the
  bus up and report health.
- **License & consent gating** in routing: enforces non-commercial use for **GHOST**
  (CC BY-NC-SA 4.0) and explicit user consent for **Heretic** (AGPL-3.0).

#### Integrations (`integrations/`)
- **22 integration adapter scaffolds** with a uniform interface
  (`connect`, `list_tools`, `call_tool`, `ping`, `close`, `build()`), each with
  `config.example.toml`, `requirements.txt`, and a feature README:
  airllm, agency_agents, bananas, cadam, ego_lite, ghost, ha_mcp, heretic,
  hivetalk_sfu, img2threejs, leanctx, lnd, longcat_video, marketing_agent,
  opencodereview, osiris, scrapling, shopstr, speech_to_speech, trycomp_crm,
  videoagent, voxcpm, worldmonitor.
- **AirLLM** configured as the primary local inference backend; cloud APIs are
  fallback only.
- Heretic ships a `CONSENT.md` gate documenting the explicit opt-in.

#### Multi-OS deployment (`nixos/`, `platforms/`)
- **NixOS / PeaceOS**: `flake.nix` plus six modules — `peace-protocols`, `mcp-bus`,
  `inference`, `voice`, `intel`, `commerce`.
- **Windows 11**: `platforms/windows/install.ps1`.
- **macOS**: Homebrew formula `platforms/macos/peace-protocols.rb`.

#### Tests & tooling (`tests/`, `scripts/`)
- `tests/test_mcp_bus.py` — 8 tests covering registry loading, tool routing, and
  license gating (8/8 passing).
- `scripts/run-v2-tests.sh` — registry validation + bus smoke tests.
- `scripts/validate_mcp_registry.py` — standalone registry validator (0 errors).

#### Documentation (`docs/`)
- `docs/v2-upgrade.md` — the v2 architecture and rollout guide.
- `docs/LICENSE-COMPLIANCE.md` — per-integration license posture and obligations.

#### Packaging
- Root `pyproject.toml` (`pip install -e .`), consolidated `requirements.txt`, and
  this `CHANGELOG.md`.

### Changed
- `README.md` and `ARCHITECTURE.md` rewritten to describe the v2 architecture
  (Agent Zero layer + Unified MCP Bus).
- `.gitignore` extended to cover live integration `config.toml` files and Python
  packaging/build artifacts.

### Notes
- **Nostr kinds** added: `30106` (Audit) and `30110` (Email).
- The v2 deliverable is a **production-shaped scaffold**: wiring, adapters, and
  environment configs are complete, but live operation requires upstream services
  (GPUs, API keys, daemons) to be provisioned per each integration's README.

## [1.0.0] — 2026-07-26

### Added
- Initial Peace Protocols scaffold: the 20-agent Raven Council constellation
  (`agents/`), master math indexes (Pe, CVI, Sr) and the 19 domain-index
  calculators (`math/`), the 6D-loop workflows (`workflows/`), foundational
  documents (`whitepaper/`, VISION, ARCHITECTURE, AGENTS), and repository
  governance (LICENSE, CONTRIBUTING, CODE_OF_CONDUCT).

[2.0.0]: https://github.com/peaceengineer0001/peace-protocols/releases/tag/v2.0.0
[1.0.0]: https://github.com/peaceengineer0001/peace-protocols/releases/tag/v1.0.0
