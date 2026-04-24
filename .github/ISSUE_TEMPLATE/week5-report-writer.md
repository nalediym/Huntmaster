---
name: "Week 5 – Report writer"
about: "Track Week 5 roadmap work: complete the report writer (PRD §3, §6)"
title: "Week 5: Report writer"
labels: ["week-5", "report-writer"]
assignees: ""
---

## PRD Reference
§3 — Report Writer, §6 Build Order Week 5

## Goal
Flesh out the `report_writer` module so it produces complete, reviewable HackerOne-style Markdown drafts and includes a prompt template for the external LLM report writer (Devin / Claude Code via Agent Vault).

## Tasks

- [ ] Add prompt template (`report_writer/prompt_template.txt` or similar) used to guide the external report writer
- [ ] Ensure `draft_report()` produces all required HackerOne report sections: Summary, Vulnerability Details, Steps to Reproduce, Proof of Concept, Impact, Remediation, Supporting Evidence
- [ ] Add tests that assert every required section is present in the output
- [ ] Add a test for findings where `poc` or `evidence` is `None` — ensure report still renders safely
- [ ] Coverage ≥ 60% for `src/report_writer/`

## Acceptance Criteria
- All required report sections present in output
- Prompt template exists and is referenced in code
- Edge cases (missing poc/evidence) handled without raising exceptions
- `ruff check .`, `mypy src/`, `pytest` all pass

## Safety Checklist
- [ ] No exploit code added
- [ ] No secrets committed
- [ ] All API calls route through Agent Vault
- [ ] `scope_enforcer/` unchanged OR human-reviewed with tests
- [ ] Tests were not modified to make them pass
