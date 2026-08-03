# 🕊️ Peace Protocols — Raven Network

> **Peace is an engineering problem.** Download the Raven Network, answer Raven's onboarding questions, and 20 sovereign AI agents immediately begin measuring, optimizing, and defending every dimension of your life — and your community's — toward mathematically-proven abundance.

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Built on Buzz](https://img.shields.io/badge/built%20on-block%2Fbuzz-orange.svg)](https://github.com/block/buzz)
[![Nostr Native](https://img.shields.io/badge/protocol-Nostr%20NIP--01-purple.svg)](https://github.com/nostr-protocol/nips)
[![Agents](https://img.shields.io/badge/agents-20-green.svg)](AGENTS.md)
[![Version](https://img.shields.io/badge/version-0.1.0--MVP-lightgrey.svg)](#)
[![Sovereignty](https://img.shields.io/badge/data-local--first-brightgreen.svg)](#-data-sovereignty)

---

## 🌍 What Is This?

The **Peace Protocols Raven Network** is an open-source, self-hostable desktop application that forks the [Buzz agent workspace](https://github.com/block/buzz) and pre-loads it with **20 custom AI agents** — 19 domain specialists and one orchestrating Chief of Staff named **Raven** — each programmed to measure, optimize, and defend a specific area of human sovereignty as defined by the [Peace Protocols whitepaper](whitepaper/Peace_Protocols.pdf) by **Raven Rolland Gregg** (Keetá Yeìl of the Lukaaẋ.ádi Clan).

The core premise: **scarcity is not a natural condition — it is the outcome of extractive, centralized system design.** The Peace Protocols define 19 measurable areas of human life — **7 Sovereign Bodies** (inner sovereignty) and **12 Resource Realms** (outer sovereignty) — and provide mathematical formulas to measure and optimize each. The Raven Network deploys AI agents to apply these protocols continuously, recursively, and at scale — from a single individual to a 7,777-member global network.

---

## 🧭 Core Design Principles

- 🔐 **Sovereignty-first** — All user data stays local or on a relay you control. Nothing leaves without explicit consent.
- 📖 **Open by default** — Apache 2.0. Every agent prompt, formula, and config is visible and forkable.
- 🕸️ **Federated by design** — Extends Buzz's Nostr-native, relay-gated architecture. Scales from one person to a global network without changing the protocol.
- ♻️ **Recursively self-improving** — Every agent runs the 6D loop (Discover → Decipher → Design → Develop → Deploy → Defend), compounding gains over time.
- 📐 **Multi-scale** — The same 20-agent stack operates identically for an individual, couple, family, clan, tribe, congregation, business, or nation.

---

## 🤖 The Raven Council — 20 Agents

### The Master Orchestrator

| # | Agent | Domain | Index | Channel |
|---|---|---|---|---|
| 20 | **🐦‍⬛ Raven** | Chief of Staff — Orchestrator | Peace Efficiency Index (Pe) + CVI | `#raven-command` |

### 7 Sovereign Bodies (Inner Sovereignty)

| # | Agent | Domain | Index | Channel |
|---|---|---|---|---|
| 1 | **✨ Starfire** | Spiritual Body — Coherence with Source | Spiritual Coherence Index (Sc) | `#starfire-spiritual` |
| 2 | **🦉 Sage** | Mental Body — Systems Literacy | Information Flow Efficiency (IFE) | `#sage-mental` |
| 3 | **🌊 River** | Emotional Body — Heart Coherence | HRV Coherence (HRVcoh) | `#river-emotional` |
| 4 | **🪨 Stone** | Physical Body — Resource Security | Local Resource Autonomy (LRA) | `#stone-physical` |
| 5 | **🔥 Ember** | Economic Body — Freedom from Debt | Debt Freedom Ratio (DFR) | `#ember-economic` |
| 6 | **🌲 Cedar** | Cultural Body — Identity and Story | Cultural Continuity Index (CCI) | `#cedar-cultural` |
| 7 | **⛰️ Summit** | Political Body — Decentralized Governance | Sovereignty Participation Ratio (SPR) | `#summit-political` |

### 12 Resource Realms (Outer Sovereignty)

| # | Agent | Domain | Index | Channel |
|---|---|---|---|---|
| 8 | **☀️ Sol** | Energy Realm | Energy Autonomy Ratio (EAR) | `#sol-energy` |
| 9 | **💧 Tide** | Water Realm | Water Sovereignty Index (WSI) | `#tide-water` |
| 10 | **🌱 Root** | Food Realm | Local Nutrition Ratio (LNR) | `#root-food` |
| 11 | **❤️‍🩹 Heal** | Health Realm | Wellness Autonomy Index (WAI) | `#heal-health` |
| 12 | **🏠 Haven** | Shelter Realm | Housing Independence Score (HIS) | `#haven-shelter` |
| 13 | **🔄 Cycle** | Waste Realm | Circularity Index (CI) | `#cycle-waste` |
| 14 | **📚 Lore** | Education Realm | Knowledge Liberation Index (KLI) | `#lore-education` |
| 15 | **🕸️ Mesh** | Communication Realm | Freedom of Flow Ratio (FFR) | `#mesh-communication` |
| 16 | **🚢 Passage** | Transportation Realm | Mobility Autonomy Fraction (MAF) | `#passage-transportation` |
| 17 | **⚒️ Forge** | Manufacturing Realm | Regenerative Production Ratio (RPR) | `#forge-manufacturing` |
| 18 | **🌾 Thrive** | Economics Realm | Abundance Finance Index (AFI) | `#thrive-economics` |
| 19 | **⚖️ Council** | Governance Realm | Justice Coherence Index (JCI) | `#council-governance` |

> Full agent guide with system prompts, intake questions, and MCP connection instructions: **[AGENTS.md](AGENTS.md)**

---

## 🚀 Quick Start

```bash
# 1. Clone with the Buzz submodule
git clone --recurse-submodules https://github.com/peaceengineer0001/peace-protocols.git
cd peace-protocols

# 2. Run the one-command setup (installs deps, initializes Buzz, configures agents)
./scripts/setup.sh

# 3. Launch the Raven Network
./scripts/launch-raven.sh
```

On first launch, **Raven** greets you and runs the onboarding sequence:

1. **Scope Selection** — Who are we optimizing for? (Individual → Nation)
2. **Identity Context** — Your name, location, lineage/tradition (optional)
3. **Domain Intake** — Each of the 19 agents collects its baseline data
4. **Baseline Calculation** — Raven computes your initial **Pe** and **CVI** scores
5. **Priority Identification** — Your three highest-leverage opportunities
6. **Activation** — The 6D loop begins across all domains

See the full walkthrough in **[docs/getting-started.md](docs/getting-started.md)**.

---

## 📐 Scope Levels

The same 20-agent stack scales across **9 levels of human organization**:

| Level | Description | Typical First Focus |
|---|---|---|
| **Individual** | Single person | DFR, LRA, EAR |
| **Couple** | Two partners | HIS, AFI, Sc |
| **Family** | Nuclear family (~6) | LNR, HIS, KLI |
| **House** | Extended/communal household | EAR, WSI, CI |
| **Clan** | Extended family network (~30) | LNR, MAF, AFI |
| **Tribe** | Community/neighborhood (~150) | All 12 realms, SPR |
| **Church Congregation** | Spiritual community | Sc, CCI, AFI, WAI |
| **Business** | Organization/enterprise | EAR, RPR, AFI, FFR |
| **Nation** | Large community/nation-state | All 19 domains + λ₂ |

Configure your scope in **[docs/scope-selector.md](docs/scope-selector.md)**.

---

## 📊 The Master Metrics

**Peace Efficiency Index** — the sum of regenerative output over dependency across all 12 realms:

```
Pe = Σ (Rᵢ / Dᵢ)   for i = 1..12
```

**Community Vitality Index** — the ratio of vitality drivers to depletion drivers:

```
CVI = (H + Dg + F) / (S + Db + De)
```

Learn the math: [Pe](docs/math/peace-efficiency-index.md) · [CVI](docs/math/community-vitality-index.md) · [Stability Theorem](docs/math/stability-theorem.md) · [Resilience Delta](docs/math/resilience-delta.md)

---

## 🔐 Data Sovereignty

All measurement data is stored **locally by default** on a Buzz relay running on your own machine. Four privacy tiers let you decide exactly what — if anything — is ever shared:

- **Tier 1 — Local Only** (default): nothing leaves the device
- **Tier 2 — Self-Hosted Relay**: sync across *your* devices only
- **Tier 3 — Chapter Relay**: opt-in sharing with a Peace Engineer chapter
- **Tier 4 — Keystone Node**: anonymized aggregate indices only

Sensitive domains (**Ember** financial data, **River** biometric data) are always Tier 1 unless you actively promote them.

---

## 🏗️ Architecture

The Raven Network is a **content and configuration overlay** on top of Buzz. We do **not** modify Buzz source — Buzz is included as a git submodule and we layer Peace Protocols agents, workflows, math, and custom Nostr kinds (`30100–30105`) on top.

See **[ARCHITECTURE.md](ARCHITECTURE.md)** for the full technical design.

---

## ⚡ v2 Upgrade — Agent Capability Layer & 22 Integrations

The **v2 upgrade** (branch `feature/v2-upgrades`) layers an **Agent Zero
capability layer** on top of the Buzz substrate and connects **22 upstream
capabilities** through a new **Unified MCP Bus**:

- 🧠 **Massive local inference** — [AirLLM](integrations/airllm/) is the
  **primary** backend (frontier models on consumer GPUs); cloud APIs are
  fallback only.
- 🗣️ **Voice** — [VoxCPM](integrations/voxcpm/) TTS +
  [Speech-to-Speech](integrations/speech_to_speech/) realtime pipeline.
- 🕸️ **Web & context** — [Scrapling](integrations/scrapling/),
  [LeanCTX](integrations/leanctx/) (60–90% token reduction),
  [Ego-Lite](integrations/ego_lite/), [OpenCodeReview](integrations/opencodereview/).
- 🌐 **Situational awareness** — [World Monitor](integrations/worldmonitor/),
  [OSIRIS](integrations/osiris/), [ha-mcp](integrations/ha_mcp/) smart home.
- 🎬 **Media & design** — [VideoAgent](integrations/videoagent/),
  [LongCat-Video](integrations/longcat_video/), [CADAM](integrations/cadam/),
  [img2threejs](integrations/img2threejs/), [HiveTalk SFU](integrations/hivetalk_sfu/),
  [Bananas](integrations/bananas/).
- 💸 **Community economy** — [Shopstr](integrations/shopstr/) +
  [LND](integrations/lnd/) Nostr Bitcoin commerce.
- 🖥️ **Multi-OS** — reference **NixOS "PeaceOS"** (`nixos/`), **Windows 11**
  (`platforms/windows/`), and **macOS Homebrew tap** (`platforms/macos/`).

The bus (`mcp_bus/`) provides concurrent connections, health monitoring,
auto-reconnection, fault isolation, and **license/consent gating**
(GHOST is non-commercial; Heretic is consent-gated and off by default).

> 🚧 The 22 integrations ship as **production-shaped scaffolds** — adapter
> contract, config, and bus registration are in place and unit-tested; live
> tool calls require the upstream service to be installed/running. See
> **[docs/v2-upgrade.md](docs/v2-upgrade.md)**, **[integrations/README.md](integrations/README.md)**,
> and **[docs/LICENSE-COMPLIANCE.md](docs/LICENSE-COMPLIANCE.md)**.

```bash
pip install pyyaml pytest
python3 scripts/validate_mcp_registry.py   # validate the 23-server registry
python3 -m mcp_bus.serve --once            # bring the bus up, print health
python3 -m pytest tests/ -v                # bus unit tests (8/8)
```

---

## 📄 Whitepaper & Documents

The foundational documents live in **[whitepaper/](whitepaper/)**:

- **[Peace_Protocols.pdf](whitepaper/Peace_Protocols.pdf)** — the foundational whitepaper
- **[Peace_Protocols_Citations.pdf](whitepaper/Peace_Protocols_Citations.pdf)** — citation bundle
- **[Peace_Protocols_Review_Comments.pdf](whitepaper/Peace_Protocols_Review_Comments.pdf)** — third-party mathematical review
- **[PEACE_Ecosystem_Master_Business_Plan.pdf](whitepaper/PEACE_Ecosystem_Master_Business_Plan.pdf)** — ecosystem master plan
- **[PEACE_Ecosystem_Executive_Teaser.pdf](whitepaper/PEACE_Ecosystem_Executive_Teaser.pdf)** — executive teaser
- **[PEACE_Ecosystem_Org_Structure.pdf](whitepaper/PEACE_Ecosystem_Org_Structure.pdf)** — organizational structure

---

## 🤝 Contributing

We welcome contributions from any Peace Engineer or aligned developer. Read **[CONTRIBUTING.md](CONTRIBUTING.md)** and our **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)** (respect · reciprocity · regeneration).

---

## 📜 License

Licensed under the **Apache License 2.0** — same as [block/buzz](https://github.com/block/buzz). See **[LICENSE](LICENSE)**.

Chosen intentionally: maximum compatibility, minimum friction for adoption by governments, indigenous communities, NGOs, and businesses.

---

<div align="center">

**Peace Engineers LLC** · [PeaceProtocols.org](https://peaceprotocols.org)

*"7,777 without hierarchy" — implemented in software.*

</div>
