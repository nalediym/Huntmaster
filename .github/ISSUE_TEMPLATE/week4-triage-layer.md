---
name: "Week 4 – Triage layer"
about: "Track Week 4 roadmap work: complete the triage layer (PRD §3, §6)"
title: "Week 4: Triage layer"
labels: ["week-4", "triage"]
assignees: ""
---

## PRD Reference
§3 — Triage Layer, §6 Build Order Week 4

## Goal
Complete the `triage` module so it checks CVSS threshold, duplicate risk, evidence quality, policy compliance, and stores a structured triage reason.

## Tasks

- [ ] Add duplicate-risk check — compare asset + finding title against stored local history; return `needs_human_review` if a near-match exists
- [ ] Add evidence-quality checklist — reject if both `evidence` and `poc` are absent
- [ ] Add policy compliance check — read program's `instruction` field; block if policy prohibits automated testing or the vulnerability class
- [ ] Store triage reason in a structured format (add `triage_reason` field to the result dict)
- [ ] Add `asset_activity` check stub (placeholder that logs "not yet implemented")
- [ ] Add `program_activity` check stub (placeholder that logs "not yet implemented")
- [ ] Coverage ≥ 80% for `src/triage/`

## Acceptance Criteria
- `triage_finding()` returns a structured dict with `triage_status`, `reason`, `scope_decision`, and `next_action`
- Duplicate, evidence-quality, and policy checks all have unit tests
- `ruff check .`, `mypy src/`, `pytest` all pass

## Safety Checklist
- [ ] No exploit code added
- [ ] No secrets committed
- [ ] All API calls route through Agent Vault
- [ ] `scope_enforcer/` unchanged OR human-reviewed with tests
- [ ] Tests were not modified to make them pass
