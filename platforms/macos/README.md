# Peace Protocols — macOS Deployment

macOS is a **parity target** covering both Intel (x86_64) and Apple Silicon
(arm64). Distribution is via a **Homebrew tap** (`homebrew-peaceprotocols`).

## Quick start

```bash
brew tap peaceengineer0001/peaceprotocols
brew install peace-protocols          # core stack
# optional integrations:
brew install peace-airllm peace-voxcpm peace-worldmonitor
```

## Apple Silicon advantages (from spec §5.3)

- **AirLLM** uses native **MLX** for Apple Silicon inference acceleration.
- **VoxCPM** can use the `llama.cpp` GGUF backend on the **Apple Neural Engine**
  — CPU/Metal inference with no discrete GPU.
- **Speech-to-Speech** ships MPS (Metal Performance Shaders) support and
  `mlx`, `mlx-audio`, `mlx-lm` dependencies.
- **Ego-Lite** runs natively (macOS is its primary platform).
- **World Monitor** ships a native Tauri desktop app (universal binary).
- **OpenCodeReview** and **LeanCTX** ship universal macOS binaries.

## Alternative: Nix on macOS

The Nix package manager runs on macOS, so users who prefer a declarative setup
can reuse the same expressions as the NixOS reference distribution
(`nixos/flake.nix`) via `nix develop`.

## The tap

`homebrew-peaceprotocols/Formula/peace-protocols.rb` is the core formula.
Per-integration formulae (`peace-<name>.rb`) install optional components with
pre-compiled bottles for both architectures.

> 🚧 **Scaffold note:** `sha256` in the formula is a placeholder filled at
> release time by CI (`brew audit --new`). Each integration still requires its
> upstream service (see `integrations/<name>/README.md`).
