## Summary

<!-- 1-2 sentences describing what this PR does and why. -->

---

## Change type

- [ ] Bug fix
- [ ] New feature
- [ ] Refactor (no behavior change)
- [ ] Tests only
- [ ] Documentation only
- [ ] CI / tooling / configuration
- [ ] Dependency update
- [ ] Other (describe below)

---

## ⚠️ Safety review required

> If this PR touches **scope enforcement**, **finding triage**, **report generation**,
> **program policy handling**, **the human review gate**, or **any submission logic**,
> it **requires human review before merge**. CI passing alone is not sufficient.

- [ ] **Does this PR alter scope enforcement logic?**
  - If yes: property-based tests (Hypothesis) are required and a human reviewer must approve.
- [ ] **Does this PR add or modify scanning, exploit, bypass, stealth, or autonomous submission logic?**
  - If yes: this PR is out of scope and will be closed.

---

## Safety checklist

- [ ] No exploit code added.
- [ ] No secrets, tokens, API keys, or real program data committed.
- [ ] All external API calls route through Agent Vault (no direct credentials).
- [ ] `src/scope_enforcer/` is unchanged **OR** I have added property-based tests and flagged for human review.
- [ ] The human approval gate for HackerOne submissions is preserved.
- [ ] No test was modified to make it pass — code was fixed instead.

---

## Testing checklist

- [ ] New or updated unit tests added.
- [ ] Property-based tests (Hypothesis) added if `scope_enforcer/` was changed.
- [ ] All external APIs mocked — no live network calls in tests.
- [ ] `pytest --cov=src --cov-report=term-missing` passes locally.
- [ ] Coverage floors met: `scope_enforcer/` ≥ 85%, others ≥ 70%.

---

## Documentation checklist

- [ ] Docstrings added or updated for changed public functions/classes.
- [ ] `docs/` updated if public-facing behavior changed.
- [ ] `AGENTS.md` or `CLAUDE.md` updated if agent rules changed (requires human review).

---

## AI-generated code

- [ ] This PR contains AI-generated code. *(If checked, human review is strongly encouraged.)*

---

## PRD reference

Section §___ — <!-- link or section name, e.g. "§5.1 HackerOne Connector" -->

---

## Open questions

<!-- List anything that needs human input or a decision before merge. -->
- [ ]
