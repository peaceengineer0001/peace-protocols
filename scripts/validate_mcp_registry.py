#!/usr/bin/env python3
"""
Validate config/mcp_servers.yaml and the integration scaffolds.

Checks:
  1. The registry parses and every server spec is structurally valid.
  2. Every `adapter`-transport server points at an importable adapter module
     that exposes a build()/*Adapter and the MCPClientProtocol methods.
  3. Every integration directory has the required scaffold files.
  4. License gates are coherent (non-commercial/consent flags set correctly).

Exit code 0 = OK, non-zero = problems found. Safe to run in CI.
"""

from __future__ import annotations

import importlib
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from mcp_bus.registry import load_registry  # noqa: E402

REQUIRED_FILES = ["__init__.py", "adapter.py", "config.example.toml", "requirements.txt", "README.md"]
CLIENT_METHODS = ["connect", "list_tools", "call_tool", "ping", "close"]


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    registry = load_registry()
    errors.extend(registry.validate())

    print(f"Loaded {len(registry)} servers "
          f"({len(registry.native())} native, {len(registry.adapters())} adapters)")

    for spec in registry:
        # License coherence
        if spec.license == "CC-BY-NC-SA-4.0" and spec.commercial_use:
            errors.append(f"{spec.name}: CC-BY-NC-SA-4.0 must set commercial_use: false")
        if spec.name == "heretic" and not spec.consent_required:
            errors.append("heretic: must set consent_required: true")

        # Adapter importability
        if spec.adapter:
            try:
                mod = importlib.import_module(spec.adapter)
            except Exception as exc:
                errors.append(f"{spec.name}: cannot import adapter {spec.adapter}: {exc!r}")
                continue
            client = None
            if hasattr(mod, "build"):
                try:
                    client = mod.build(spec)
                except Exception as exc:
                    errors.append(f"{spec.name}: build() failed: {exc!r}")
            if client is not None:
                for m in CLIENT_METHODS:
                    if not hasattr(client, m):
                        errors.append(f"{spec.name}: adapter client missing method '{m}'")

    # Integration directory scaffolds
    integ_root = os.path.join(REPO, "integrations")
    for name in sorted(os.listdir(integ_root)):
        d = os.path.join(integ_root, name)
        if not os.path.isdir(d) or name.startswith("__"):
            continue
        for fn in REQUIRED_FILES:
            if not os.path.exists(os.path.join(d, fn)):
                errors.append(f"integrations/{name}: missing {fn}")
        if name == "heretic" and not os.path.exists(os.path.join(d, "CONSENT.md")):
            errors.append("integrations/heretic: missing CONSENT.md")

    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    for w in warnings:
        print("  WARN:", w)
    for e in errors:
        print("  ERROR:", e)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
