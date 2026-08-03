# 🏗️ ARCHITECTURE — How Peace Protocols Layers on Buzz

The Peace Protocols Raven Network is a **content and configuration overlay** on top of [block/buzz](https://github.com/block/buzz). We do **not** fork or modify Buzz's source code. Buzz is included as a **git submodule**, and the Raven Network adds a small, well-contained set of Peace Protocols artifacts on top: agent personas, YAML workflows, math calculators, scope logic, and a handful of custom Nostr event kinds.

This design keeps us a good citizen of the Buzz ecosystem — upstream improvements flow straight through to us — while giving Peace Engineers a fully-loaded, sovereignty-first workspace out of the box.

---

## 1. Layered System Overview

```
┌──────────────────────────────────────────────────────────────┐
│                     RAVEN NETWORK CLIENTS                       │
│                                                                │
│   Desktop App (Tauri 2 + React 19)      Mobile (Flutter)       │
│   ┌───────────────────────────────┐     [future — follows      │
│   │  Peace Protocols UI Overlay   │      Buzz Flutter release]  │
│   │  • Scope Selector             │                             │
│   │  • Peace Mandala Dashboard    │                             │
│   │  • Pe / CVI Score Gauges      │                             │
│   │  • 20 Agent Channel Views     │                             │
│   │  • 6D Loop Progress Tracker   │                             │
│   └───────────────────────────────┘                            │
└──────────────────────────────────────────────────────────────┘
                    │ WebSocket (NIP-01)
                    ▼
┌──────────────────────────────────────────────────────────────┐
│                    buzz-relay (Rust)  [submodule]              │
│  NIP-01 · NIP-42 auth · MCP agent interface · Audit log        │
│  ┌──────────────────────────────────────────────────────┐     │
│  │        Peace Protocols Extensions (overlay)          │     │
│  │  • Custom Nostr kinds 30100–30105 (Pe/CVI/6D/scope)  │     │
│  │  • 20 pre-configured agent personas                  │     │
│  │  • 6D loop workflow definitions (YAML)               │     │
│  │  • Scope-level community isolation config            │     │
│  └──────────────────────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────────┘
         │                    │                    │
    ┌────▼────┐          ┌────▼────┐         ┌────▼────┐
    │Postgres │          │  Redis  │         │S3/MinIO │
    │(events) │          │(pub/sub)│         │(Blossom)│
    └─────────┘          └─────────┘         └─────────┘
```

**What Buzz provides:** the relay, Nostr protocol handling, MCP agent runtime, NIP-42 authentication, Workflows engine, Canvases, Communities, Teams, Buzz Mesh compute pooling, and the Tauri/React desktop shell.

**What Peace Protocols adds:** the 20 agents, their prompts and intake flows, the 6D workflows, the Pe/CVI/index math, the scope-selector logic, the Peace Mandala dashboard components, and the custom Nostr kinds that carry Peace Protocol measurements.

---

## 2. Custom Nostr Event Kinds (30100–30105)

All Peace Protocol measurements are ordinary Nostr events, signed with the user's secp256k1 keypair and stored in the Buzz relay's event store. We use a dedicated block in the **parameterized replaceable event** range so that the latest measurement of any kind is always addressable, while history remains available via the audit log.

| Kind | Name | Purpose | Key `tags` |
|---|---|---|---|
| **30100** | Pe Score Event | Peace Efficiency Index measurement | `d`=scope-id, `pe`, `period` |
| **30101** | CVI Score Event | Community Vitality Index measurement | `d`=scope-id, `cvi`, `H`,`Dg`,`F`,`S`,`Db`,`De` |
| **30102** | Domain Index Event | A single realm/body index (EAR, DFR, …) | `d`=domain-id, `index`, `value`, `agent` |
| **30103** | 6D Loop State Event | Current 6D phase for an agent/domain | `d`=domain-id, `phase`, `agent`, `cycle` |
| **30104** | Scope Configuration Event | The user's scope level and community members | `d`=scope-id, `level`, `members` |
| **30105** | Coherence Shock Event | Raven-coordinated community event | `d`=event-id, `type`, `starts_at`, `delta` |

### Example — Kind 30102 (Domain Index Event) for Sol/EAR

```json
{
  "kind": 30102,
  "pubkey": "<sol-agent-pubkey>",
  "created_at": 1753400000,
  "tags": [
    ["d", "energy"],
    ["index", "EAR"],
    ["value", "0.42"],
    ["agent", "sol"],
    ["scope", "individual:npub1..."],
    ["phase", "decipher"]
  ],
  "content": "{\"E_local\":4200,\"E_demand\":10000,\"notes\":\"rooftop solar, no storage\"}",
  "sig": "<schnorr-signature>"
}
```

Because these events live in a high, application-specific kind range, **any other Nostr client safely ignores them** — the Raven Network remains fully interoperable with the wider Nostr network.

---

## 3. Peace Protocols "Crates" (Logical Modules)

Following the whitepaper's tech-stack plan, the Peace Protocols layer is organized as logical modules. In the MVP these are implemented as configuration + Python calculators; the Phase-2 roadmap ports the hot paths to Rust crates that compile alongside Buzz.

| Module | MVP Location | Target Rust Crate | Responsibility |
|---|---|---|---|
| **agents** | [`agents/`](agents/) | `peace-protocols-agents` | 20 pre-configured personas: prompts, intake, config |
| **math** | [`math/`](math/) | `peace-protocols-math` | Pe, CVI, Sr, and the 19 domain-index calculators |
| **scope** | [`config/scope-config.example.toml`](config/scope-config.example.toml) | `peace-protocols-scope` | Scope-selector logic and multi-level aggregation |
| **workflows** | [`workflows/`](workflows/) | (Buzz Workflows engine) | 6D loop definitions as YAML-as-code |
| **onboarding** | [`agents/raven/intake_questions.md`](agents/raven/intake_questions.md) | React component | Raven-guided onboarding wizard |
| **dashboard** | (UI overlay) | React component | Peace Mandala, Pe/CVI gauges, trend charts |

---

## 4. Data Model

Every node stores its data in the Buzz relay running on `localhost` by default:

```
User's Local Relay (buzz-relay on localhost:4736)
├── User keypair (secp256k1) ......... encrypted at rest
├── Scope configuration .............. Kind 30104 events
├── Domain measurements (×19) ........ Kind 30102 events
├── 6D loop states ................... Kind 30103 events
├── Pe / CVI history ................. Kind 30100 / 30101 events
├── Coherence shocks ................. Kind 30105 events
├── Agent outputs .................... standard Nostr notes in agent channels
└── Canvases ......................... one living document per agent domain
```

**Time-series:** because Pe, CVI, and each domain index are emitted as timestamped events, trend charts and the Resilience Delta (`Sr`) are computed directly from event history — no separate database schema is required.

**Cross-agent synthesis:** Raven subscribes to all 30102 (Domain Index) events, aggregates the 12 realm terms into `Pe`, derives the six CVI inputs from the relevant body/realm indices, and publishes the 30100/30101 master events.

---

## 5. Scope Federation

Each **scope level** (Individual → Nation) is a Buzz **Community** with its own relay-enforced isolation (NIP-42). Federation is **voluntary and additive**:

```
individual:npub1abc...   ──(aggregate 30100/30101 only)──►  family:npub1fam...
family:npub1fam...       ──(aggregate 30100/30101 only)──►  tribe:npub1tri...
tribe:npub1tri...        ──(anonymized aggregates)────────►  keystone (7,777)
```

Rules enforced by the scope module:

1. **Raw domain data (30102) never leaves its origin scope** unless the owner explicitly promotes its `privacy_tier`.
2. **Only aggregate 30100/30101 events flow upward.** A parent scope sees the child's Pe/CVI totals, never the underlying inputs.
3. **Commands never flow downward.** A parent scope cannot write to a child scope's event store; it can only read the aggregates the child chooses to publish.
4. **Every hop is signed and auditable.** The Buzz audit log records exactly which aggregate crossed which relay and when.

This is the software realization of the whitepaper's **"7,777 without hierarchy"** — sovereignty preserved at every node, coherence achievable across the mesh, and no capturable apex.

---

## 6. Why an Overlay (Not a Hard Fork)

- **Upstream compatibility:** Buzz improvements (performance, security, mobile) reach us for free.
- **Auditability:** our entire delta from vanilla Buzz is the contents of this repository — reviewable in one place.
- **Portability:** the 20 agents are ordinary Buzz agents; a user could run them on any Buzz relay.
- **Trust:** sovereignty-conscious users can diff our overlay against upstream Buzz and verify exactly what Peace Protocols adds.

See [`.gitmodules`](.gitmodules) for the Buzz submodule pin, and [ARCHITECTURE decisions in the whitepaper](whitepaper/Peace_Protocols.pdf) for the full rationale.



---

## 7. v2 — Agent Capability Layer & Unified MCP Bus

v2 **extends** (does not replace) the overlay architecture above. Two things are
added:

### 7.1 Agent Zero capability layer
A new capability layer built on a fork of **Agent Zero** is inserted between the
client UI and the Buzz relay. It contributes a Docker-sandboxed XFCE Linux
desktop, Chromium browser automation with DOM annotation, LibreOffice document
co-working, and multi-agent delegation. Crucially, it speaks the **same MCP
interface** the overlay already uses, so Buzz remains the substrate (identity,
transport, relay runtime, audit) while Agent Zero adds capability. This is why
both statements are true: *Peace Protocols is a Buzz overlay* **and** *v2 forks
Agent Zero* — they operate at different layers.

```
 Client UI
    │
 Agent Zero capability layer   (sandboxed desktop, browser, docs, delegation)
    │  ── Unified MCP Bus ──►   22 integration MCP servers
 Buzz / Nostr relay            (substrate: identity, transport, audit, workspace)
```

### 7.2 Unified MCP Bus (`mcp_bus/`)
A hub-and-spoke bus. Agent Zero is the central MCP client; each integration is
an independent MCP server (6 native + 17 adapters). The
[`MCPConnectionPool`](mcp_bus/pool.py) provides:

- **concurrent** startup of all enabled servers,
- **health monitoring** with exponential-backoff **auto-reconnection**,
- **fault isolation** — a failing integration is contained,
- **routing** — `find_tool` / `call_tool` dispatch to the owning server,
- **license & consent gating** — non-commercial servers (GHOST) are skipped
  under a commercial deployment; consent-gated servers (Heretic) stay down until
  explicit, logged consent.

The registry is declared in
[`config/mcp_servers.yaml`](config/mcp_servers.yaml) and parsed by
[`mcp_bus/registry.py`](mcp_bus/registry.py).

### 7.3 New Nostr kinds
v2 introduces kind `30106` (audit events, incl. Heretic consent) and `30110`
(email bridge), extending the v1 range `30100–30105`.

### 7.4 Inference routing
**AirLLM is the primary inference backend** (weight/expert streaming); cloud
APIs are fallback only. Context is compressed through **LeanCTX** (60–90% token
reduction) before reaching any model, preserving both sovereignty and cost.

See [docs/v2-upgrade.md](docs/v2-upgrade.md) for the full v2 design, honest
implementation status, and the multi-OS deployment matrix.
