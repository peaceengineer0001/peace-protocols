# PeaceOS core module — Agent Zero capability layer + Buzz/Nostr substrate.
{ config, lib, pkgs, ... }:

with lib;
let
  cfg = config.services.peaceProtocols;
in
{
  options.services.peaceProtocols = {
    enable = mkEnableOption "Peace Protocols Raven Network";

    user = mkOption {
      type = types.str;
      default = "raven";
      description = "System user the Peace Protocols services run as.";
    };

    dataDir = mkOption {
      type = types.path;
      default = "/var/lib/peace-protocols";
      description = "State directory for relay data, keypairs and measurement stores.";
    };

    scope = mkOption {
      type = types.enum [
        "individual" "family" "tribe" "community"
        "bioregion" "nation" "continental" "global" "keystone"
      ];
      default = "individual";
      description = "Peace Protocols operating scope (drives agent configuration).";
    };
  };

  config = mkIf cfg.enable {
    users.users.${cfg.user} = {
      isSystemUser = true;
      group = cfg.user;
      home = cfg.dataDir;
      createHome = true;
    };
    users.groups.${cfg.user} = { };

    # Agent Zero capability layer runs the Docker-sandboxed desktop; the Buzz
    # Nostr client provides the relay/runtime substrate.
    virtualisation.docker.enable = true;

    systemd.services.peace-agent-zero = {
      description = "Peace Protocols — Agent Zero capability layer";
      wantedBy = [ "multi-user.target" ];
      after = [ "network.target" "docker.service" ];
      serviceConfig = {
        User = cfg.user;
        WorkingDirectory = cfg.dataDir;
        Environment = [ "PEACE_SCOPE=${cfg.scope}" ];
        # Reference invocation; the Agent Zero fork is fetched/pinned by the
        # inference & mcp-bus modules.
        ExecStart = "${pkgs.nodejs_22}/bin/node ./agent-zero/server.js";
        Restart = "on-failure";
        RestartSec = 5;
      };
    };

    environment.systemPackages = with pkgs; [ python313 nodejs_22 git ];
  };
}
