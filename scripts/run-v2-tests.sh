#!/usr/bin/env bash
# Run the Peace Protocols v2 checks: registry validation, bus smoke test, unit tests.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "🕊️  Peace Protocols v2 — validation suite"
echo "=========================================="

python3 -c "import yaml" 2>/dev/null || { echo "Installing pyyaml..."; pip install --quiet pyyaml; }

echo
echo "==> 1/3 Validate MCP server registry + integration scaffolds"
python3 scripts/validate_mcp_registry.py

echo
echo "==> 2/3 MCP bus smoke test (bring up, print health, exit)"
python3 -m mcp_bus.serve --once >/dev/null && echo "    bus started and shut down cleanly ✅"

echo
echo "==> 3/3 Unit tests"
if python3 -c "import pytest" 2>/dev/null; then
  python3 -m pytest tests/ -q
else
  python3 tests/test_mcp_bus.py
fi

echo
echo "✅ v2 validation complete."
