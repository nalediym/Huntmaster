---
name: "Week 3 – Manual JSON finding import"
about: "Track Week 3 roadmap work: complete the finding importer (PRD §3, §6)"
title: "Week 3: Manual JSON finding import"
labels: ["week-3", "finding-importer"]
assignees: ""
---

## PRD Reference
§3 — Manual Finding Import, §6 Build Order Week 3

## Goal
Finalise the `finding_importer` so it validates scope before storage, rejects incomplete findings with clear errors, and is fully tested including malformed JSON.

## Tasks

- [ ] Document the finding input schema (JSON Schema or Pydantic model in `models.py`)
- [ ] Add scope validation in `import_finding()` — pass a `ScopeEnforcer` and reject assets that don't return `ALLOW`
- [ ] Reject findings where `evidence` and `poc` are both absent (insufficient quality)
- [ ] Add tests for malformed / incomplete JSON inputs
- [ ] Add contract test with a recorded fixture of a real-shaped finding JSON
- [ ] Coverage ≥ 70% for `src/finding_importer/` (target 80%)

## Acceptance Criteria
- `import_finding()` rejects out-of-scope assets, missing required fields, and invalid CVSS
- Malformed JSON handled gracefully with `FindingImportError`
- All tests pass with mocked scope enforcer
- `ruff check .`, `mypy src/`, `pytest` all pass

## Safety Checklist
- [ ] No exploit code added
- [ ] No secrets committed
- [ ] All API calls route through Agent Vault
- [ ] `scope_enforcer/` unchanged OR human-reviewed with tests
- [ ] Tests were not modified to make them pass
