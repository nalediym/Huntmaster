# Huntmaster — Agent Instructions

> These rules apply to every AI coding agent that operates in this repository:
> GitHub Copilot, Devin, Claude Code, or any future agent. They are non-negotiable.

---

## 1. Project mission

Huntmaster is a **human-approved security research orchestration pipeline** for authorized
HackerOne bug bounty workflows. It parses scope data, validates assets against an explicit
allow/deny policy, ingests structured finding JSON, triages findings, drafts reports, and
routes everything to a human review queue. No step is automated past the human gate.

---

## 2. Safety boundaries (hard limits — never override)

| Rule | Detail |
|---|---|
| No exploit code | Exploitation lives exclusively in Pensar Apex. Do not add attack logic here. |
| No scope bypass | Never weaken, disable, or add exceptions to `src/scope_enforcer/`. |
| No auto-submit | Every HackerOne submission requires explicit human approval through the review queue. |
| No secrets in source | Tokens, API keys, passwords, and real program data must never be committed. |
| Agent Vault only | All external API calls (HackerOne, Pensar, Devin, OpenRouter) must route through Agent Vault. Never use direct credentials. |
| No offensive logic | Do not add: credential attacks, bypass techniques, stealth/evasion logic, autonomous scanning, payload libraries, destructive test cases, or real-user data collection. |

If any ambiguity exists around scope, authorization, safety, or real-user data — **block and
request human review**. Do not guess. Do not proceed.

---

## 3. What agents may build

Agents may autonomously add or modify:

- Scope parsing and allow/deny-list validation logic (with tests and human review for `scope_enforcer/`)
- Policy checks and audit logging
- Finding JSON parsing and normalization
- Severity scoring and duplicate-risk triage
- Report drafting and formatting
- Human review queue workflows
- HackerOne connector (read-only)
- CLI tooling
- Tests and documentation

---

## 4. What agents must never build

- Exploit modules of any kind
- Credential attacks or stuffing
- Bypass or evasion techniques
- Autonomous scanning or active probing
- Autonomous submission (no auto-submit to HackerOne)
- Stealth or anti-detection logic
- Payload libraries
- PII collection or storage
- Web dashboards or mobile app features (v0.2+)

---

## 5. Modules and review requirements

### Safe to modify autonomously

`src/h1_connector/`, `src/report_writer/`, `src/review_queue/`, `src/finding_importer/`,
`tests/`, `docs/`

### Requires human review before merge

`src/scope_enforcer/`, `src/triage/`, `db/schema.sql`, `SECURITY.md`, `AGENTS.md`

Any PR touching these modules must:
1. Include property-based tests (Hypothesis) for `scope_enforcer/`.
2. Add a clear "Safety checklist" section in the PR description.
3. Not be merged without an explicit human approval (not just a passing CI run).

---

## 6. Coding standards

- **Language:** Python 3.11+
- **Package manager:** `uv`
- **HTTP:** `httpx`
- **Data models:** `pydantic` v2
- **CLI:** `click`
- **Lint/format:** `ruff` (line length 100)
- **Types:** `mypy` (strict where feasible)
- All public functions must have type annotations.
- Prefer small, focused modules with clear interfaces.
- No bare `except:` — catch specific exceptions.
- No mutable default arguments.

---

## 7. Testing expectations

- Every behavior change ships with tests.
- `src/scope_enforcer/` requires **85% coverage** and property-based tests with Hypothesis.
  - Generate random asset strings; verify no out-of-scope asset ever passes.
  - Wildcards must behave correctly; ambiguous scope must always block.
- All other modules require **70% coverage**.
- All external APIs must be mocked (`responses` library or `unittest.mock`). No live network calls in tests.
- **Never modify a test to make it pass.** Fix the code. If the test is genuinely wrong, explain why in the PR description and request human review.

Run locally:
```bash
ruff check .
mypy src/
pytest --cov=src --cov-report=term-missing
```

---

## 8. Documentation expectations

- Public functions and classes must have docstrings.
- Non-obvious logic must have inline comments.
- Update `docs/` when changing public-facing behavior.
- PR descriptions must include: summary, PRD reference, what was built, what was tested,
  coverage summary, and a safety checklist.

---

## 9. PR size and style

- Prefer small PRs (≤ 400 lines of diff).
- Split large changes into logical, independently-reviewable PRs.
- One concern per PR — do not combine feature, refactor, and test in the same PR.
- Commit messages: `type(scope): short description` (e.g., `feat(triage): add severity scorer`).

---

## 10. How agents should handle ambiguity

1. Re-read `docs/PRD.md`, `CLAUDE.md`, `SECURITY.md`, and this file.
2. If still ambiguous: implement the **safest possible** minimal stub (not a full feature) and
   open a draft PR titled `blocked: [reason]` explaining exactly what is unclear.
3. Never guess on anything related to: scope authorization, safety boundaries, real-user data,
   or offensive security logic.

---

## 11. Self-heal loop (3-attempt rule)

**Attempt 1:** Run `ruff check --fix`, run `mypy src/`, re-read the failing test. Fix the code. Retry.

**Attempt 2:** Re-read `docs/PRD.md`. Simplify — smaller diff, clearer intent. Retry.

**Attempt 3:** Re-read `AGENTS.md` and `CLAUDE.md`. Try the simplest possible implementation. Retry.

**After 3 failed attempts:** Stop. Open draft PR titled `blocked: [reason]`. Explain what you tried,
what failed, and what you need from a human reviewer.

---

## 12. Cloud agent priority

1. **GitHub Copilot coding agent** — assign `@copilot` to any issue
2. **Devin** — Slack DM workflow
3. **Claude Code** — fallback / deep refactors

All agents follow the rules in this file and `CLAUDE.md`.
