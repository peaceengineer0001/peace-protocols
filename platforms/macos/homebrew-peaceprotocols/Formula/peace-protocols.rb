# Peace Protocols v2 — macOS Homebrew formula (core stack).
#
# Tap:      brew tap peaceengineer0001/peaceprotocols
# Install:  brew install peace-protocols
#
# Targets Intel (x86_64) and Apple Silicon (arm64) via a universal install.
# Apple Silicon gains native MLX inference (AirLLM), native Ego-Lite, and
# Tauri desktop packaging for World Monitor. Optional integrations ship as
# separate formulae in this tap (see Formula/peace-*.rb).
class PeaceProtocols < Formula
  desc "Raven Network — sovereign multi-agent life & community optimization system"
  homepage "https://github.com/peaceengineer0001/peace-protocols"
  url "https://github.com/peaceengineer0001/peace-protocols/archive/refs/tags/v2.0.0.tar.gz"
  # NOTE: sha256 is filled in at release time by `brew audit --new`/CI.
  sha256 "0000000000000000000000000000000000000000000000000000000000000000"
  license "Apache-2.0"
  version "2.0.0"

  depends_on "python@3.13"       # ha-mcp, AirLLM, VoxCPM
  depends_on "node@22"           # Agent Zero fork, Ego-Lite, Buzz client
  depends_on "go"                # LND, OpenCodeReview binaries
  depends_on "git"

  # Apple Silicon inference acceleration.
  on_macos do
    on_arm do
      depends_on "libomp"
    end
  end

  def install
    # Core stack: mcp_bus, agent configs, math, workflows, docs.
    libexec.install Dir["*"]
    (bin/"peace-protocols").write <<~SH
      #!/bin/bash
      export PEACE_HOME="#{libexec}"
      exec "#{Formula["python@3.13"].opt_bin}/python3" -m mcp_bus.serve "$@"
    SH
    chmod 0755, bin/"peace-protocols"
  end

  def caveats
    <<~EOS
      Peace Protocols core is installed.

      1. Create your live configs:
           cd #{libexec} && for f in config/*.example.toml; do cp "$f" "${f%.example.toml}.toml"; done
      2. Start the Unified MCP Bus:
           peace-protocols
      3. Optional integrations (install as needed from this tap):
           brew install peace-airllm peace-voxcpm peace-worldmonitor ...

      Apple Silicon: AirLLM uses native MLX; VoxCPM can use the llama.cpp GGUF
      backend on the Apple Neural Engine (no discrete GPU required).

      GHOST is CC BY-NC-SA 4.0 (non-commercial). CADAM and Shopstr are GPL-3.0.
      See docs/LICENSE-COMPLIANCE.md.
    EOS
  end

  test do
    assert_predicate libexec/"config/mcp_servers.yaml", :exist?
    system Formula["python@3.13"].opt_bin/"python3", "-c",
           "import sys; sys.path.insert(0, '#{libexec}'); import mcp_bus; print(mcp_bus.__version__)"
  end
end
