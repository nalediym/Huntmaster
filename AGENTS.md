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

## Self-heal loop

3 attempts → open draft PR titled `blocked: [reason]`, stop.
