# PeaceOS module — VoxCPM TTS + Speech-to-Speech pipeline.
# Voice pillar: VoxCPM (TTS) and the HuggingFace Speech-to-Speech realtime
# pipeline (VAD->STT->LLM->TTS). The LLM stage points at the AirLLM backend.
{ config, lib, pkgs, ... }:

with lib;
let
  cfg = config.services.peaceProtocols.voice;
in
{
  options.services.peaceProtocols.voice.enable =
    mkEnableOption "VoxCPM TTS + Speech-to-Speech pipeline";

  config = mkIf cfg.enable {
    # Reference port(s) around 8632; adjust in config/mcp_servers.yaml.
    systemd.services.peace-voxcpm = {
      description = "Peace Protocols — VoxCPM TTS";
      wantedBy = [ "multi-user.target" ];
      after = [ "peace-airllm.service" ];
      serviceConfig = {
        ExecStart = "${pkgs.python313}/bin/python3 -m voxcpm.server --port 8632";
        Restart = "on-failure";
      };
    };
    systemd.services.peace-speech-to-speech = {
      description = "Peace Protocols — Speech-to-Speech realtime pipeline";
      wantedBy = [ "multi-user.target" ];
      after = [ "peace-airllm.service" "peace-voxcpm.service" ];
      serviceConfig = {
        Environment = [ "S2S_LLM_ENDPOINT=http://127.0.0.1:8631/v1" "S2S_TTS_ENDPOINT=http://127.0.0.1:8632/v1" ];
        ExecStart = "${pkgs.python313}/bin/python3 -m speech_to_speech.server --port 8633";
        Restart = "on-failure";
      };
    };
  };
}
