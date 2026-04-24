---
name: "Week 1 – HackerOne connector + DB schema"
about: "Track Week 1 roadmap work: read-only H1 client and database schema (PRD §3, §6)"
title: "Week 1: HackerOne connector + DB schema"
labels: ["week-1", "h1-connector", "db"]
assignees: ""
---

## PRD Reference
§3 — HackerOne Connector, §6 Build Order Week 1

## Goal
Stand up the read-only HackerOne API client and the SQLite database schema so that programs and their structured scope can be fetched and persisted.

## Tasks

- [ ] Complete `db/schema.sql` — add `programs` and `scope_assets` tables (D1-compatible)
- [ ] Implement `HackerOneClient.list_programs()` — fetch program metadata via API
- [ ] Implement `HackerOneClient.get_structured_scope()` — fetch structured scope for a program
- [ ] Add `Program` Pydantic v2 model alongside the existing `ScopeAsset` model
- [ ] Add `StoredProgram` / `StoredScopeAsset` round-trip tests (mock API with `responses`)
- [ ] Verify all external calls route through Agent Vault (not direct credentials)

## Acceptance Criteria
- `h1_connector` can fetch and return program metadata and scope (read-only)
- Schema is normalized, persisted in SQLite, D1-compatible
- All external API calls mocked in tests (`responses` library)
- Coverage ≥ 70% for `src/h1_connector/`
- `ruff check .`, `mypy src/`, `pytest` all pass

## Safety Checklist
- [ ] No exploit code added
- [ ] No secrets committed
- [ ] All API calls route through Agent Vault
- [ ] `scope_enforcer/` unchanged OR human-reviewed with tests
- [ ] Tests were not modified to make them pass
