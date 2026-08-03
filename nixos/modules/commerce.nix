# PeaceOS module — Community economy (LND, Shopstr, HiveTalk SFU).
# Community economy pillar. LND provides Lightning rails; Shopstr is the
# Nostr marketplace (GPL-3.0); HiveTalk SFU is Nostr-native conferencing
# (AGPL-3.0). See docs/LICENSE-COMPLIANCE.md.
{ config, lib, pkgs, ... }:

with lib;
let
  cfg = config.services.peaceProtocols.commerce;
in
{
  options.services.peaceProtocols.commerce.enable =
    mkEnableOption "Community economy (LND, Shopstr, HiveTalk SFU)";

  config = mkIf cfg.enable {
    # Reference port(s) around 8080; adjust in config/mcp_servers.yaml.
    systemd.services.peace-lnd = {
      description = "Peace Protocols — Lightning Network Daemon";
      wantedBy = [ "multi-user.target" ];
      serviceConfig = {
        ExecStart = "${pkgs.lnd}/bin/lnd";
        Restart = "on-failure";
      };
    };
    # Shopstr + HiveTalk run as containerized services on the Nostr layer.
    virtualisation.docker.enable = true;
  };
}
