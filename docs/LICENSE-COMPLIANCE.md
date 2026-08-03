# License Compliance — v2 Integrations

Peace Protocols is **Apache-2.0**. The v2 upgrade wires in 22 upstream projects,
**none of which are vendored** — each is installed out-of-band from its own
repository, and Peace Protocols ships only thin MCP adapters plus configuration.
This document records the license obligations that apply.

## Summary matrix

| Integration | License | Class | Obligation for Peace Protocols |
|---|---|---|---|
| AirLLM | Apache-2.0 | Permissive | Attribution; NOTICE |
| Agency Agents | MIT | Permissive | Attribution |
| VoxCPM | Apache-2.0 | Permissive | Attribution; NOTICE |
| Speech-to-Speech | Apache-2.0 | Permissive | Attribution; NOTICE |
| Scrapling | BSD-3-Clause | Permissive | Attribution; no-endorsement |
| OpenCodeReview | Apache-2.0 | Permissive | Attribution; NOTICE |
| Ego-Lite | MIT | Permissive | Attribution |
| LeanCTX | Apache-2.0 | Permissive | Attribution; NOTICE |
| **World Monitor** | **AGPL-3.0** | Strong copyleft (network) | Any modified network service must be offered under AGPL-3.0 |
| ha-mcp | MIT | Permissive | Attribution |
| OSIRIS | MIT | Permissive | Attribution |
| TryComp CRM | MIT | Permissive | Attribution |
| **GHOST** | **CC BY-NC-SA 4.0** | **NON-COMMERCIAL** + ShareAlike | **No commercial use**; attribution; ShareAlike |
| **Heretic** | **AGPL-3.0** | Strong copyleft (network) | AGPL-3.0 for network derivatives; **+ consent policy** |
| VideoAgent | MIT | Permissive | Attribution |
| Bananas | MIT | Permissive | Attribution |
| **HiveTalk SFU** | **AGPL-3.0** | Strong copyleft (network) | Any modified network service must be offered under AGPL-3.0 |
| LongCat-Video | MIT | Permissive | Attribution |
| **CADAM** | **GPL-3.0** | Strong copyleft | Derivative works must remain GPL-3.0 |
| img2threejs | Apache-2.0 | Permissive | Attribution; NOTICE |
| **Shopstr** | **GPL-3.0** | Strong copyleft | Derivative works must remain GPL-3.0 |
| LND | MIT | Permissive | Attribution |

## Key obligations & how we honor them

### GHOST — CC BY-NC-SA 4.0 (NON-COMMERCIAL)
GHOST may **not** be used for commercial purposes. Enforcement in this repo:
- In `config/mcp_servers.yaml`, GHOST is marked `commercial_use: false`.
- The MCP bus (`mcp_bus/pool.py`) is constructed with `allow_commercial`. When a
  deployment declares itself commercial, the pool **skips** every server whose
  `commercial_use` is false — GHOST never starts.
- ShareAlike: any modifications to GHOST itself must be shared under the same
  license.

### AGPL-3.0 — World Monitor, Heretic, HiveTalk SFU
AGPL's network clause means if we **modify** any of these and offer it as a
network service, we must publish the modified source under AGPL-3.0. Because we
only call them across the MCP boundary (separate processes/services) and do not
modify them, our Apache-2.0 code is not itself made AGPL. If a deployer forks
and modifies any of these, they inherit the AGPL obligation. This is compatible
with — and welcomed by — the Peace Protocols open-source mission.

### GPL-3.0 — CADAM, Shopstr
Derivative works of GPL-3.0 code must remain GPL-3.0. We integrate them as
separate services across MCP/HTTP boundaries (mere aggregation), so the
Apache-2.0 license of this repository is preserved. Do **not** copy GPL-3.0
source into the Peace Protocols codebase.

### Heretic — additional consent policy
Beyond AGPL-3.0, Heretic is governed by
[`integrations/heretic/CONSENT.md`](../integrations/heretic/CONSENT.md): off by
default, consent-gated, local models only, consent logged to Nostr kind `30106`.

## Attribution
A consolidated `NOTICE` entry and per-integration attribution live in each
`integrations/<name>/README.md`. When distributing binaries (Homebrew bottles,
Windows installer, NixOS closures), include the upstream license texts for any
component actually bundled.
