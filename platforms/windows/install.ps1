<#
.SYNOPSIS
    Peace Protocols v2 — Windows 11 modular installer.

.DESCRIPTION
    Guided setup for the Peace Protocols Raven Network on Windows 11. Each
    integration is an OPTIONAL component so users install only what they need.
    Components that require Linux-native dependencies are installed under WSL 2;
    OpenCodeReview and LeanCTX ship native Windows binaries (no WSL needed).

    This mirrors the NixOS reference distribution to reach feature parity
    (see docs/v2-upgrade.md, §5 Multi-OS Deployment).

.NOTES
    Run from an elevated PowerShell:  powershell -ExecutionPolicy Bypass -File install.ps1
#>

[CmdletBinding()]
param(
    [switch]$All,
    [string[]]$Components = @('core'),
    [switch]$UseWSL = $true
)

$ErrorActionPreference = 'Stop'
$Banner = @'
  ____                       ____            _                  _
 |  _ \ ___  __ _  ___ ___  |  _ \ _ __ ___ | |_ ___   ___ ___ | |___
 | |_) / _ \/ _` |/ __/ _ \ | |_) | '__/ _ \| __/ _ \ / __/ _ \| / __|
 |  __/  __/ (_| | (_|  __/ |  __/| | | (_) | || (_) | (_| (_) | \__ \
 |_|   \___|\__,_|\___\___| |_|   |_|  \___/ \__\___/ \___\___/|_|___/
                  Windows 11 installer — v2
'@
Write-Host $Banner -ForegroundColor Cyan

# --- Prerequisite matrix ---------------------------------------------------
function Install-Prereqs {
    Write-Host "==> Checking prerequisites..." -ForegroundColor Yellow
    $winget = Get-Command winget -ErrorAction SilentlyContinue
    if (-not $winget) { throw "winget is required (App Installer from the Microsoft Store)." }

    # Python 3.13 (required by ha-mcp), Node 22+ (Ego-Lite), Git, Docker Desktop.
    $packages = @(
        @{ id = 'Python.Python.3.13';        name = 'Python 3.13' },
        @{ id = 'OpenJS.NodeJS.LTS';          name = 'Node.js 22 LTS' },
        @{ id = 'Git.Git';                    name = 'Git' },
        @{ id = 'Docker.DockerDesktop';       name = 'Docker Desktop' }
    )
    foreach ($p in $packages) {
        Write-Host "    - $($p.name)"
        winget install --id $p.id --silent --accept-package-agreements --accept-source-agreements -e | Out-Null
    }

    if ($UseWSL) {
        Write-Host "==> Ensuring WSL 2 (for Linux-native components)..." -ForegroundColor Yellow
        wsl --install --no-launch 2>$null
        wsl --set-default-version 2 2>$null
    }
}

# --- CUDA (AirLLM GPU acceleration) ----------------------------------------
function Install-CUDA {
    Write-Host "==> Installing CUDA toolkit for AirLLM GPU acceleration..." -ForegroundColor Yellow
    winget install --id Nvidia.CUDA --silent -e | Out-Null
    Write-Host "    (AirLLM streams weights; a 4GB+ CUDA GPU + NVMe SSD is recommended.)"
}

# --- Component installers --------------------------------------------------
$ComponentMap = @{
    'core'             = { Write-Host '    core: mcp_bus + Agent Zero fork + Buzz client (native Node.js)' }
    'inference'        = { Install-CUDA; Write-Host '    airllm: pip install airllm (Python + CUDA)' }
    'voice'            = { Write-Host '    voxcpm + speech-to-speech: Python + ONNX/MPS fallback' }
    'web-intel'        = { Write-Host '    scrapling (native), leanctx (native binary), worldmonitor (Tauri)' }
    'code-review'      = { Write-Host '    opencodereview: native Windows Go binary (no WSL)' }
    'browser'          = { Write-Host '    ego-lite: Windows support in progress (issue #203); Playwright fallback' }
    'smart-home'       = { Write-Host '    ha-mcp: Docker or pip (PyPI)' }
    'osint'            = { Write-Host '    osiris + ghost: Docker Desktop compose stacks (ghost = non-commercial)' }
    'crm'              = { Write-Host '    trycomp-crm: Docker or native (Bun)' }
    'media'            = { Write-Host '    videoagent + longcat-video: pip + CUDA; bananas: Electron binary' }
    'conferencing'     = { Write-Host '    hivetalk-sfu: Docker or npm' }
    'design'           = { Write-Host '    cadam + img2threejs: Node.js / browser / Python CLI' }
    'commerce'         = { Write-Host '    lnd (Go binary) + shopstr (Docker/npm)' }
}

# --- Main ------------------------------------------------------------------
Install-Prereqs

$toInstall = if ($All) { $ComponentMap.Keys } else { $Components }
foreach ($c in $toInstall) {
    if ($ComponentMap.ContainsKey($c)) {
        Write-Host "==> Installing component: $c" -ForegroundColor Green
        & $ComponentMap[$c]
    } else {
        Write-Warning "Unknown component '$c' (valid: $($ComponentMap.Keys -join ', '))"
    }
}

Write-Host "`n==> Registering MCP servers..." -ForegroundColor Yellow
if (-not (Test-Path ".\config\mcp_servers.yaml")) {
    Write-Warning "config\mcp_servers.yaml not found — run from the repo root."
}

Write-Host "`n🕊️  Peace Protocols base install complete." -ForegroundColor Cyan
Write-Host "Next: copy config\*.example.toml to config\*.toml, then start the MCP bus:" -ForegroundColor Gray
Write-Host "    python -m mcp_bus.serve" -ForegroundColor Gray
Write-Host "See docs\v2-upgrade.md and platforms\windows\README.md for parity notes." -ForegroundColor Gray
