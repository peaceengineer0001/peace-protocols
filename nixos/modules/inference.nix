# PeaceOS module — AirLLM local inference (primary).
# AirLLM is the PRIMARY inference backend. Weight/expert streaming lets
# frontier models run on modest VRAM. CUDA + NVMe are strongly recommended;
# the module wires GPU passthrough and the CUDA toolkit.
{ config, lib, pkgs, ... }:

with lib;
let
  cfg = config.services.peaceProtocols.inference;
in
{
  options.services.peaceProtocols.inference.enable =
    mkEnableOption "AirLLM local inference (primary)";

  config = mkIf cfg.enable {
    # Reference port(s) around 8631; adjust in config/mcp_servers.yaml.
    # GPU / CUDA for AirLLM weight streaming.
    hardware.graphics.enable = true;
    nixpkgs.config.cudaSupport = lib.mkDefault true;

    systemd.services.peace-airllm = {
      description = "Peace Protocols — AirLLM inference server (OpenAI-compatible)";
      wantedBy = [ "multi-user.target" ];
      after = [ "network.target" ];
      serviceConfig = {
        WorkingDirectory = "/var/lib/peace-protocols";
        # Model weights are large (100GB+); stored on fast NVMe (see hardware reqs).
        Environment = [ "AIRLLM_MODEL=kimi-k3" "AIRLLM_COMPRESSION=mxfp4" ];
        ExecStart = "${pkgs.python313}/bin/python3 -m airllm.server --port 8631";
        Restart = "on-failure";
      };
    };
    environment.systemPackages = with pkgs; [ python313 ];
  };
}
