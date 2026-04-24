# PRD: Huntmaster / APEX-LOOP

**Author:** Naledi  
**Status:** Draft v0.1  
**Date:** April 23, 2026  
**Codename:** `APEX-LOOP`

## 1. Problem Statement

Bug bounty hunting is high-skill, high-time-cost work. A researcher must manually browse programs, evaluate scope, enumerate attack surface, run tests, triage findings, write structured reports, and track outcomes.

The opportunity is a human-gated pipeline that reduces repetitive work while keeping legal, ethical, and safety controls in the center of the architecture.

## 2. Product Vision

> Point the pipeline at authorized program data. Come back to a queue of draft reports, pre-validated, pre-formatted, ready for human review.

The system can learn from outcomes over time, but v0.1 is intentionally conservative and human-triggered.

## 3. Core Modules

### HackerOne Connector

Read-only by default. Pulls program metadata and structured scope for authorized programs.

### Scope Enforcer

Ensures no downstream workflow operates on assets outside explicit program scope.

Hard rules:

- If asset type is not allow-listed, block.
- If asset is explicitly out of scope, block.
- If scope is ambiguous, block and flag for human review.
- All decisions are logged.

### Manual Finding Import

Consumes structured JSON findings from an external authorized testing process. v0.1 does not trigger autonomous scanning.

### Triage Layer

Checks scope, duplicate risk, CVSS threshold, evidence quality, asset activity, program activity, and policy compliance.

### Report Writer

Produces reviewable HackerOne-style Markdown drafts.

### Review Queue

Human-in-the-loop approval flow for approve, edit, reject, and log feedback.

## 4. MVP Scope

### In scope

- HackerOne API connector, read-only
- Scope Enforcer with logging
- Manual finding JSON import
- Triage
- Report drafting
- CLI review queue

### Out of scope

- Auto-submission
- Fully autonomous scanning
- Mobile testing
- Program scoring
- Learning loop
- Bounty dashboard

## 5. Success Metrics

| Metric | 90-day target |
|---|---:|
| Programs reviewed | ≥ 10 |
| Valid findings drafted | ≥ 5 |
| Reports submitted manually | ≥ 3 |
| First bounty paid | ≥ $1 |
| Duplicate rate | < 30% |
| False positive rate | < 20% |
| Finding-to-draft time | < 30 minutes |

## 6. Build Order

| Week | Focus |
|---|---|
| 1 | HackerOne API connector + DB schema |
| 2 | Scope Enforcer |
| 3 | Manual JSON import + parsing |
| 4 | Triage layer |
| 5 | Report writer + prompt tuning |
| 6 | CLI review queue + first authorized live test |
