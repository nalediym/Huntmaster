---
name: "Week 6 – CLI review queue + first live workflow"
about: "Track Week 6 roadmap work: CLI review queue and first authorized live test (PRD §3, §6)"
title: "Week 6: CLI review queue + first authorized live workflow"
labels: ["week-6", "review-queue", "cli"]
assignees: ""
---

## PRD Reference
§3 — Review Queue, §6 Build Order Week 6

## Goal
Build the CLI on top of the existing `ReviewQueue` backend so that Naledi can list, view, approve, edit, or reject draft reports from the terminal — and then run the first authorized end-to-end workflow.

## Tasks

- [ ] Add `cli.py` (Click-based) with commands: `list`, `view <index>`, `approve <index>`, `reject <index> --reason`, `edit <index> --notes`
- [ ] Wire `ReviewQueue` backend to CLI commands
- [ ] Log every review action (timestamp, action, notes) to a local audit file or the SQLite DB
- [ ] Add tests for each CLI command using Click's `CliRunner`
- [ ] Prepare checklist for first authorized live workflow (authorized program, human in the loop at every step)
- [ ] Coverage ≥ 70% for `src/review_queue/`

## Acceptance Criteria
- CLI commands (`list`, `view`, `approve`, `reject`, `edit`) all work end-to-end
- Audit trail written for every review action
- No report is ever auto-submitted — all paths require explicit human approval
- `ruff check .`, `mypy src/`, `pytest` all pass

## Safety Checklist
- [ ] No exploit code added
- [ ] No secrets committed
- [ ] All API calls route through Agent Vault
- [ ] `scope_enforcer/` unchanged OR human-reviewed with tests
- [ ] Tests were not modified to make them pass
