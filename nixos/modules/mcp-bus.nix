# PeaceOS module — Unified MCP Bus.
# Brings up the mcp_bus connection pool as a systemd service. It reads
# config/mcp_servers.yaml and maintains concurrent, health-monitored
# connections to every enabled integration MCP server.
{ config, lib, pkgs, ... }:

with lib;
let
  cfg = config.services.peaceProtocols.mcpBus;
in
{
  options.services.peaceProtocols.mcpBus.enable =
    mkEnableOption "Unified MCP Bus";

  config = mkIf cfg.enable {
    # Reference port(s) around 8600; adjust in config/mcp_servers.yaml.
    systemd.services.peace-mcp-bus = {
      description = "Peace Protocols — Unified MCP Bus (connection pool)";
      wantedBy = [ "multi-user.target" ];
      after = [ "network.target" ];
      serviceConfig = {
        WorkingDirectory = "/var/lib/peace-protocols";
        Environment = [ "PEACE_MCP_SERVERS=/etc/peace-protocols/mcp_servers.yaml" ];
        ExecStart = "${pkgs.python313}/bin/python3 -m mcp_bus.serve";
        Restart = "on-failure";
      };
    };
    environment.systemPackages = [ pkgs.python313 pkgs.python313Packages.pyyaml ];
  };
}
