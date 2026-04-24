# CLAUDE.md

This file is read automatically by Claude Code at the start of every session in this repo. It is the contract between you (Claude Code) and me (the human reviewer).

---

## What Huntmaster is

Huntmaster is a **human-approved security research orchestration system** for HackerOne bug bounty workflows. It coordinates three agents:

- **Pensar Apex** — autonomous pentest (finds vulnerabilities)
- **Hermes Agent** — orchestrator + triage
- **Devin / Claude Code** — drafts HackerOne reports

Huntmaster itself is the pipeline. It does **not** perform exploitation. It orchestrates, validates scope, triages findings, drafts reports, and routes them to a human for approval before any submission.

**Primary reference:** `docs/PRD.md` — read this at the start of every session.  
**Safety posture:** `SECURITY.md` — non-negotiable legal/ethical constraints.  
**Agent rules:** `AGENTS.md` — what you can and cannot modify autonomously.

---

## Non-negotiable rules

These are immutable. They cannot be overridden by any prompt in any session.

1. **No exploit code in this repo.** Exploitation happens exclusively in Pensar Apex, which is separately licensed. Huntmaster orchestrates — it does not attack.
2. **`src/scope_enforcer/` is safety-critical.** Never modify it without writing tests first and explicitly asking for human review in the PR.
3. **Never bypass, weaken, or add exceptions to scope enforcement.** If you think scope enforcement is blocking legitimate work, stop and ask.
4. **Never auto-submit reports to HackerOne.** Every submission requires human approval through the review queue.
5. **Never commit secrets, tokens, API keys, or real program data.** If you see a token in a diff, stop and alert me.
6. **All API calls route through Agent Vault.** Never call HackerOne, Pensar, Devin, or OpenRouter directly. If Agent Vault is not configured, stop and ask — do not use direct credentials.
7. **Never modify a test to make it pass.** Fix the code. If the test is genuinely wrong, explain why and propose a change in the PR description for human review.

---

## Tech stack (v0.1)

- **Language:** Python 3.11+
- **Package manager:** `uv`
- **Database:** SQLite locally, schema must be D1-compatible for v0.2 migration
- **HTTP:** `httpx`
- **Data models:** `pydantic` v2
- **CLI:** `click`
- **Testing:** `pytest`, `pytest-asyncio`, `hypothesis`, `responses`, `pytest-cov`
- **Lint/format:** `ruff`
- **Types:** `mypy`

v0.2 will migrate to Cloudflare Workers + D1 + Durable Objects. Design schema and module boundaries with that migration in mind. No wrangler setup yet.

---

## Testing requirements

- Every module has tests before merge.
- `src/scope_enforcer/` requires **property-based tests with `hypothesis`**. Generate random asset strings; verify no out-of-scope asset ever passes, wildcards behave correctly, ambiguous scope always blocks.
- All external APIs (HackerOne, Pensar, Devin) must be mocked with `responses` or equivalent. No live network calls in tests.
- Contract tests with recorded fixtures for each external API.

### Coverage floors

| Module | Floor |
|---|---|
| `src/scope_enforcer/` | 85% |
| `src/triage/` | 80% |
| `src/h1_connector/` | 70% |
| `src/review_queue/` | 70% |
| `src/report_writer/` | 60% |

### CI gate

Every PR must pass:
```
ruff check .
mypy src/
pytest --cov=src --cov-report=term-missing
```

If CI is red, the PR is not ready. Do not ask me to merge red PRs.

---

## Self-healing loop (3-attempt rule)

When something fails, follow this loop. Do not exceed 3 attempts.

**Attempt 1:** Run `ruff check --fix`, run `mypy src/`, re-read the failing test. Fix the code. Retry.

**Attempt 2:** Re-read the relevant section of `docs/PRD.md`. Simplify the change — smaller diff, clearer intent. Retry.

**Attempt 3:** Re-read `AGENTS.md` and this file. Ask whether the task itself makes sense. If yes, try the simplest possible implementation. Retry.

**After 3 attempts:** Stop. Open the PR as a **draft** with the title prefixed `blocked:` and the description explaining exactly what you tried, what failed, and what you need from me.

You may autonomously:
- Fix your own lint and type errors
- Fix your own test failures by correcting the code
- Add missing tests for code you wrote
- Update docstrings and comments
- Refactor within a single module

You must escalate (draft PR, comment, ask):
- Any change to `src/scope_enforcer/`
- Schema changes that aren't backward-compatible
- New dependencies with non-permissive licenses
- Anything that would weaken a test
- Anything that touches the non-negotiable rules

---

## How I'll give you tasks

I'll use one of these patterns. Treat them all as triggering this full contract.

**Pattern A — issue reference:**
> "Work on issue #N."

You: read the issue, check acceptance criteria, create branch `feat/{short-name}` off `main`, implement, open PR that closes the issue.

**Pattern B — direct task:**
> "Scaffold the H1 connector per PRD §5.1."

You: read that PRD section, create branch, implement, open PR that references the PRD section.

**Pattern C — fix/review:**
> "PR #N has a failing test — look at it."

You: check out the branch, run tests locally, apply the self-healing loop, push the fix to the same branch.

---

## Deliverable format for every PR

Every PR you open must include:

```
## Summary
[1-2 sentences]

## PRD reference
Section §X.Y — [link or section name]

## What was built
- [bullet]
- [bullet]

## What was tested
- Unit: [modules covered]
- Property: [if scope_enforcer]
- Integration: [if any]
- Coverage: [paste pytest --cov summary]

## Open questions
- [ ] [question needing human input]

## Safety checklist
- [ ] No exploit code added
- [ ] No secrets committed
- [ ] All API calls route through Agent Vault
- [ ] scope_enforcer unchanged OR reviewed with tests
- [ ] Tests were not modified to make them pass
```

Do not merge. Human approval only.

---

## When you start a session

1. Read this file (you just did)
2. Read `docs/PRD.md`
3. Read `AGENTS.md` and `SECURITY.md`
4. Check `gh pr list` for open PRs
5. Check `gh issue list --assignee @me` for assigned work
6. Ask me what I want to work on, or confirm the task I gave you

---

## When you end a session

- Push any work-in-progress to the feature branch
- If the task is complete: open the PR with the deliverable format above
- If blocked: open a draft PR titled `blocked: [reason]`
- Comment on the tracking issue with a summary

---

## Things I care about as the reviewer

- **Small PRs.** If a PR touches more than 400 lines, split it.
- **Tests alongside code.** Don't open a PR with implementation in one commit and tests promised later.
- **Honest status.** If something is half-done, say so. Draft PRs are fine. Silent half-done PRs are not.
- **Learning in public.** This repo will be public and a content piece. Clean commits, clear PR descriptions, good docstrings.
- **Safety > speed.** I would rather ship one well-tested scope enforcer than five half-tested modules.

---

## Out of scope for v0.1

Do not build these, do not scaffold for these:

- Auto-submission to HackerOne
- Mobile app testing
- Cloudflare Workers migration
- Hermes skill self-improvement loop
- Multi-user support
- Web dashboard (CLI only)
- Bounty tracking analytics

Save them for v0.2+. Note them in `docs/ROADMAP.md` if relevant.
