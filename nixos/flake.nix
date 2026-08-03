{
  # ───────────────────────────────────────────────────────────────────────────
  # PeaceOS — Peace Protocols reference NixOS distribution (v2)
  # ───────────────────────────────────────────────────────────────────────────
  # NixOS is the PRIMARY / reference platform: purely functional package
  # management gives reproducible builds, atomic upgrades and rollbacks across
  # the whole stack, and pins every dependency for auditability (security model
  # §7.2 "Supply chain").
  #
  #   nix develop            # reproducible contributor dev shell
  #   nixos-rebuild switch --flake .#peaceos   # build/switch the PeaceOS system
  # ───────────────────────────────────────────────────────────────────────────
  description = "PeaceOS — the Peace Protocols Raven Network as a declarative NixOS system";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; config.allowUnfree = true; };
    in
    {
      # ── PeaceOS system configuration ──────────────────────────────────────
      nixosConfigurations.peaceos = nixpkgs.lib.nixosSystem {
        inherit system;
        modules = [
          ./modules/peace-protocols.nix
          ./modules/mcp-bus.nix
          ./modules/inference.nix        # AirLLM + GPU/CUDA
          ./modules/voice.nix            # VoxCPM + Speech-to-Speech
          ./modules/intel.nix            # World Monitor, OSIRIS, GHOST, ha-mcp
          ./modules/commerce.nix         # LND, Shopstr, HiveTalk
          ({ ... }: {
            system.stateVersion = "24.11";
            networking.hostName = "peaceos";
            # Least-privilege firewall; each module opens only what it needs.
            networking.firewall.enable = true;
          })
        ];
      };

      # ── Reproducible development shell ────────────────────────────────────
      devShells.${system}.default = pkgs.mkShell {
        name = "peace-protocols-dev";
        packages = with pkgs; [
          python313
          nodejs_22
          go
          rustc cargo
          pyyaml
          git
        ];
        shellHook = ''
          echo "🕊️  PeaceOS dev shell — Python $(python3 --version), Node $(node --version)"
          echo "Run: python3 -m pytest tests/  |  python3 scripts/validate_mcp_registry.py"
        '';
      };
    } // flake-utils.lib.eachDefaultSystem (system: {
      formatter = nixpkgs.legacyPackages.${system}.nixpkgs-fmt;
    });
}
