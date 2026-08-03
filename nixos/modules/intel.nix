# PeaceOS module — Intelligence & smart-home (World Monitor, OSIRIS, GHOST, ha-mcp).
# Intelligence pillar. OSIRIS and GHOST deploy as Docker Compose stacks;
# ha-mcp runs as a native MCP server; World Monitor uses its hosted MCP
# endpoint (or self-host). GHOST is CC BY-NC-SA 4.0 (non-commercial) and is
# only started when services.peaceProtocols.intel.enableNonCommercial = true.
{ config, lib, pkgs, ... }:

with lib;
let
  cfg = config.services.peaceProtocols.intel;
in
{
  options.services.peaceProtocols.intel.enable =
    mkEnableOption "Intelligence & smart-home (World Monitor, OSIRIS, GHOST, ha-mcp)";

  config = mkIf cfg.enable {
    # Reference port(s) around 8640; adjust in config/mcp_servers.yaml.
    options.services.peaceProtocols.intel.enableNonCommercial = lib.mkOption {
      type = lib.types.bool; default = false;
      description = "Enable GHOST (CC BY-NC-SA 4.0, non-commercial use only).";
    };

    systemd.services.peace-ha-mcp = {
      description = "Peace Protocols — Home Assistant MCP (ha-mcp)";
      wantedBy = [ "multi-user.target" ];
      serviceConfig = {
        Environment = [ "HA_URL=http://homeassistant.local:8123" ];
        ExecStart = "${pkgs.python313}/bin/python3 -m ha_mcp serve";
        Restart = "on-failure";
      };
    };
    virtualisation.docker.enable = true;   # OSIRIS / GHOST compose stacks
  };
}
