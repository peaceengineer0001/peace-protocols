# Peace Protocols — Windows 11 Deployment

Windows 11 is a **parity target** (the NixOS PeaceOS distribution is the
reference). The installer `install.ps1` provides a guided, component-based
setup.

## Quick start

```powershell
# From an elevated PowerShell, at the repo root:
powershell -ExecutionPolicy Bypass -File platforms\windows\install.ps1 -All
# ...or pick components:
powershell -ExecutionPolicy Bypass -File platforms\windows\install.ps1 -Components core,inference,web-intel
```

## What the installer sets up

| Prerequisite | Why | Source |
|---|---|---|
| Python 3.13 | ha-mcp, AirLLM, VoxCPM | winget `Python.Python.3.13` |
| Node.js 22 LTS | Agent Zero fork, Ego-Lite, Buzz | winget `OpenJS.NodeJS.LTS` |
| Docker Desktop | OSIRIS, GHOST, HiveTalk, CRM | winget `Docker.DockerDesktop` |
| CUDA toolkit | AirLLM GPU streaming | winget `Nvidia.CUDA` |
| WSL 2 | Linux-native components | `wsl --install` |

## Platform notes (from spec §5.2)

- **Native (no WSL):** OpenCodeReview and LeanCTX ship native Windows binaries.
- **WSL 2:** components needing Linux-native deps run under WSL 2.
- **Ego-Lite:** Windows support is in progress upstream (issue #203); a
  Playwright fallback is used until it lands.
- **Buzz client + Agent Zero fork:** run natively on the Node.js runtime.
- **Scrapling + MCP ecosystem:** run without platform-specific modification.

## Component matrix

`core`, `inference`, `voice`, `web-intel`, `code-review`, `browser`,
`smart-home`, `osint`, `crm`, `media`, `conferencing`, `design`, `commerce`.

> 🚧 **Scaffold note:** the installer wires prerequisites and component layout.
> Each integration still requires its upstream service (see
> `integrations/<name>/README.md`).
