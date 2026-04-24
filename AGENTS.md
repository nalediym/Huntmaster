# Huntmaster Agent Rules

1. No exploit code. Pensar Apex handles exploitation.
2. `src/scope_enforcer/` needs tests + human review before any changes.
3. No bypassing scope enforcement.
4. No auto-submit to HackerOne.
5. No committed secrets or real program data.
6. All API calls route through Agent Vault.

## Safe to modify autonomously

`h1_connector`, `report_writer`, `review_queue`, `finding_importer`, `tests/`, `docs/`

## Requires human review

`scope_enforcer/`, `triage/`, `db/schema.sql`, `SECURITY.md`

## Testing

- `pytest` + `hypothesis`. 85% coverage for `scope_enforcer`, 70% elsewhere.
- Fix code, never tests.
- All external APIs must be mocked (`responses` library).

## Cloud agent priority

Sessions are driven in this order:

1. **GitHub Copilot coding agent** (included, available now — assign `@copilot` to any issue)
2. **Devin** ($20/mo, mobile-first, Slack DM workflow)
3. **Claude Code** (fallback / deep refactors)

All agents follow the same non-negotiable rules above and the master prompt in the Launch Kit.

## Self-heal loop

3 attempts → open draft PR titled `blocked: [reason]`, stop.
