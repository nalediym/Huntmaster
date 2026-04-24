---
name: "Week 2 – Scope Enforcer"
about: "Track Week 2 roadmap work: complete scope enforcement logic (PRD §3, §6)"
title: "Week 2: Scope Enforcer"
labels: ["week-2", "scope-enforcer", "safety-critical"]
assignees: ""
---

## PRD Reference
§3 — Scope Enforcer, §6 Build Order Week 2

> ⚠️ **Safety-critical module.** Any change requires tests written first and explicit human review in the PR.

## Goal
Harden and complete the `ScopeEnforcer` so it correctly handles all decision states, enforces audit logging, and blocks all ambiguous or policy-restricted cases.

## Tasks

- [ ] Add `BLOCK_POLICY_RESTRICTED` handling — check `instruction` field for policy keywords (e.g. "no automated testing")
- [ ] Add audit logging — every `evaluate()` call must emit a structured log entry
- [ ] Add property-based tests with `hypothesis` — random asset strings, verify no out-of-scope asset ever passes, wildcards behave correctly, ambiguous scope always blocks
- [ ] Add CIDR, `ANDROID_APP`, `IOS_APP`, `OTHER` asset-type stub handlers (block with `BLOCK_UNSUPPORTED_ASSET_TYPE` for now)
- [ ] Confirm decision states match `ARCHITECTURE.md`: `ALLOW`, `BLOCK_OUT_OF_SCOPE`, `BLOCK_AMBIGUOUS`, `BLOCK_UNSUPPORTED_ASSET_TYPE`, `BLOCK_POLICY_RESTRICTED`
- [ ] Coverage ≥ 85% for `src/scope_enforcer/`

## Acceptance Criteria
- All five decision states are reachable and tested
- Audit log entry written for every call
- `hypothesis` property tests pass
- Coverage ≥ 85%
- `ruff check .`, `mypy src/`, `pytest` all pass

## Safety Checklist
- [ ] No exploit code added
- [ ] No secrets committed
- [ ] All API calls route through Agent Vault
- [ ] PR explicitly requests human review of `scope_enforcer/` changes
- [ ] Tests were not modified to make them pass
