# GitHub Copilot Instructions — Huntmaster

This is a **safety-sensitive security automation repository**. Read this file before generating
any code, tests, or documentation.

---

## Hard constraints

**Never generate:**

- Exploit logic of any kind
- Stealth or anti-detection logic
- Evasion techniques
- Credential attacks or stuffing
- Bypass logic for scope enforcement or any other safety control
- Payload libraries (shellcode, XSS payloads, SQL injection strings, etc.)
- Autonomous submission code (no auto-submit to HackerOne or any platform)
- PII collection, storage, or exfiltration
- Active scanning or probing logic

If a request could result in any of the above, implement a **safe stub**, **refusal path**,
**validation guard**, or **docs-only change** instead — then note the limitation in a comment.

---

## What to build

Prefer work in these categories:

- Defensive validation (scope enforcement, policy checks, input sanitization)
- Audit logging
- Human review queue workflows
- Structured data parsing (finding JSON, scope JSON, program metadata)
- Report drafting and text formatting
- Severity scoring and duplicate-risk triage (no active scanning)
- CLI tooling
- Tests and documentation

---

## Language and toolchain

- **Python 3.11** — use modern syntax (`match`, `tomllib`, walrus operator where clear)
- **Ruff** for linting and formatting (line length 100)
- **MyPy** for type checking — annotate all public APIs
- **Pytest** + **Hypothesis** for tests — property-based tests for scope-enforcer
- **Pydantic v2** for data models
- **httpx** for HTTP (async-friendly)
- **responses** library to mock all external HTTP calls in tests
- Package management: **uv**

---

## Code style

- All public functions and classes need type annotations and docstrings.
- No bare `except:` — catch specific exceptions.
- No mutable default arguments.
- Small, focused functions with clear names.
- Prefer `pathlib.Path` over `os.path`.
- Keep PRs small (≤ 400 lines of diff).

---

## Testing

- Every behavior change ships with tests.
- `src/scope_enforcer/` needs 85% coverage and Hypothesis property tests.
- All other modules need 70% coverage.
- Mock all external APIs — no live network calls in tests.
- **Never modify a test to make it pass.** Fix the code instead.

---

## Safety checklist (run mentally before every suggestion)

- [ ] Does this add exploit, evasion, stealth, bypass, credential attack, or scanning logic? → **Refuse or stub safely.**
- [ ] Does this touch `src/scope_enforcer/`? → **Add tests and flag for human review.**
- [ ] Does this commit a secret, token, or real program data? → **Stop. Never commit secrets.**
- [ ] Does this auto-submit to HackerOne? → **Block. Human approval always required.**
- [ ] Does this call an external API directly without Agent Vault? → **Route through Agent Vault.**
