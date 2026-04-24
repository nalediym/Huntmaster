# Huntmaster

**Human-approved bug bounty research pipeline with strict scope enforcement.**

Huntmaster is the public implementation of the APEX-LOOP PRD: a security automation research project for authorized bug bounty workflows. The v0.1 goal is intentionally narrow: ingest HackerOne program/scope data, enforce scope boundaries, parse structured finding JSON, triage findings, draft report text, and place everything into a human review queue.

> Public repo policy: this project does **not** ship exploit modules, credential attacks, bypass techniques, stealth logic, or autonomous submission logic.

## Vision

Help a researcher move from scattered manual work to a clean, auditable queue of draft reports:

1. Pull authorized program metadata and structured scope.
2. Normalize in-scope and out-of-scope assets.
3. Block anything ambiguous or out of scope.
4. Parse scanner/agent output only after scope validation.
5. Triage findings for duplicate risk, validity, severity, and evidence quality.
6. Draft a concise HackerOne-style report.
7. Require human approval before any submission.

## v0.1: Human-Gated MVP

### In scope

- HackerOne connector, read-only by default
- Scope Enforcer with audit logging
- Manual Apex JSON import, not autonomous scanning
- Hermes-style triage prompt and checklist
- Devin-style report drafting prompt
- Simple CLI review queue design
- Local SQLite-compatible schema with Cloudflare D1 migration path

### Out of scope

- Auto-submission
- Autonomous scanning
- Exploit module development
- Credential stuffing
- PII collection or storage
- Mobile app testing
- Program auto-selection
- Public disclosure tooling

## Safety principles

- Authorized programs only.
- Explicit scope only.
- Ambiguous scope means block and ask a human.
- Do not store or reproduce real user data.
- Respect program rules, including automated testing restrictions.
- Human review is required before submission.

See [`docs/ETHICS.md`](docs/ETHICS.md).

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```
