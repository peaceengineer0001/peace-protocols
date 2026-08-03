# ⚠ Heretic — Explicit Consent Required

Heretic performs **directional ablation ("abliteration")** — it removes the
refusal/safety alignment from a language model. Running it changes how a model
behaves in ways that carry legal, ethical, and safety consequences that are the
**sole responsibility of the operator**.

## Peace Protocols policy

1. **Off by default.** In `config/mcp_servers.yaml`, `heretic` is
   `enabled: false` and `consent_required: true`. The Unified MCP Bus will
   refuse to bring the adapter up unless a consent callback returns `True`.
2. **Explicit, logged consent.** The operator must set
   `consent_acknowledged = true` in `integrations/heretic/config.toml` **and**
   the runtime consent prompt must be affirmatively answered. Consent events are
   logged to the Nostr audit stream (kind `30106`).
3. **Local models only.** Heretic operates on locally-held HuggingFace weights
   run through AirLLM. No abliterated weights are uploaded or redistributed by
   Peace Protocols.
4. **Community-values alignment, not harm.** This capability exists so a
   sovereign community can align a model to its own values rather than a
   vendor's corporate policy — consistent with the Peace Protocols mission of
   self-determination. It is not provided to facilitate harm.

## License

Heretic is **AGPL-3.0**. Any network-served derivative must also be offered
under AGPL-3.0. See [`../../docs/LICENSE-COMPLIANCE.md`](../../docs/LICENSE-COMPLIANCE.md).
