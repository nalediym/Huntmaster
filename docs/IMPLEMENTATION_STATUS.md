# Implementation Status

Maps every requirement from the `/docs` files to current code state.
Updated: April 24, 2026.

---

## PRD §3 — Core Modules

| Module | PRD Requirement | Status | Notes |
|---|---|---|---|
| HackerOne Connector | Read-only — fetch programs + structured scope | 🟡 Stub | `client.py` stubs raise `NotImplementedError` |
| Scope Enforcer | Block out-of-scope, ambiguous, unsupported | 🟢 Partial | Core logic exists; missing policy-restricted check + audit log |
| Manual Finding Import | Consume structured JSON findings | 🟢 Partial | Validates required fields + CVSS; missing scope pre-check |
| Triage Layer | Scope, duplicate, CVSS, evidence, policy | 🟡 Partial | Scope + CVSS done; duplicate/evidence/policy checks missing |
| Report Writer | HackerOne-style Markdown drafts | 🟢 Done | All required sections present |
| Review Queue | Human approve / edit / reject | 🟢 Done | Backend done; CLI not yet built |

---

## ROADMAP — Week-by-Week Checklist

### Week 1: HackerOne connector + DB schema

| Task | Status |
|---|---|
| Create database schema | 🔴 Missing — `db/schema.sql` has only the PRAGMA line |
| Add environment variable loading | 🟡 `.env.example` exists; loader not wired |
| Add read-only HackerOne client stub | 🟡 Stub exists, not implemented |
| Add program/scope normalization models | 🟡 `ScopeAsset` exists; no `Program` model |
| Add tests for stored program records | 🔴 Missing |

### Week 2: Scope Enforcer

| Task | Status |
|---|---|
| Implement exact URL matching | 🟢 Done |
| Implement wildcard domain matching | 🟢 Done |
| Implement out-of-scope deny-list priority | 🟢 Done |
| Add ambiguous-scope blocking | 🟢 Done |
| Add audit logs for all decisions | 🔴 Missing |

### Week 3: Manual JSON import

| Task | Status |
|---|---|
| Define finding input schema | 🟡 Implicit in `REQUIRED_FIELDS`; no formal schema |
| Parse sample finding JSON | 🟢 Done |
| Validate findings against scope before storage | 🔴 Missing — no scope enforcer call in importer |
| Reject unsupported or incomplete findings | 🟡 Partial — CVSS + required fields; missing evidence check |
| Add tests for malformed JSON | 🟡 Partial (see `test_finding_importer.py`) |

### Week 4: Triage layer

| Task | Status |
|---|---|
| Add CVSS threshold checks | 🟢 Done |
| Add duplicate-risk check against local history | 🔴 Missing |
| Add evidence-quality checklist | 🔴 Missing |
| Add policy compliance check | 🔴 Missing |
| Store triage reason | 🟡 Partial — `reason` field in dict, not persisted to DB |

### Week 5: Report writer

| Task | Status |
|---|---|
| Add Markdown report template | 🟢 Done |
| Add prompt template for external report writer | 🔴 Missing |
| Generate report drafts from validated findings | 🟢 Done |
| Add tests for required report sections | 🟡 Partial (see `test_report_writer.py`) |

### Week 6: CLI review queue

| Task | Status |
|---|---|
| List pending draft reports | 🔴 Missing — backend exists, no CLI |
| View report details | 🔴 Missing |
| Mark approved, edited, or rejected | 🔴 Missing |
| Log rejection reasons | 🔴 Missing |
| Prepare first authorized live workflow | 🔴 Not started |

---

## ARCHITECTURE.md — Component Cross-Check

| Component | Implemented | Notes |
|---|---|---|
| HackerOne Connector | 🟡 Stub | `client.py` |
| Program + Scope Store | 🔴 No schema | `db/schema.sql` is empty |
| Scope Enforcer | 🟢 Partial | Missing `BLOCK_POLICY_RESTRICTED` + audit log |
| Manual Finding Import | 🟢 Partial | Missing scope pre-check |
| Triage Layer | 🟡 Partial | Missing duplicate/evidence/policy checks |
| Report Writer | 🟢 Done | `markdown.py` |
| Review Queue | 🟡 Backend only | No CLI yet |

### Decision states (ARCHITECTURE.md)

| State | Implemented |
|---|---|
| `ALLOW` | 🟢 Yes |
| `BLOCK_OUT_OF_SCOPE` | 🟢 Yes |
| `BLOCK_AMBIGUOUS` | 🟢 Yes |
| `BLOCK_UNSUPPORTED_ASSET_TYPE` | 🟢 Yes |
| `BLOCK_POLICY_RESTRICTED` | 🔴 Enum defined, never returned |

---

## ETHICS.md — Safety Rule Cross-Check

| Rule | Enforced in Code | Notes |
|---|---|---|
| Authorized programs only | 🟡 Manual | No automated auth check yet |
| Explicit scope only | 🟢 Yes | `ScopeEnforcer` blocks all non-matching assets |
| Ambiguous means blocked | 🟢 Yes | `BLOCK_AMBIGUOUS` is the default fallback |
| No real-user data collection | 🟢 By design | No data-collection code exists |
| Respect program policy | 🔴 Partial | `BLOCK_POLICY_RESTRICTED` not yet implemented |
| No autonomous submission | 🟢 Yes | `submit_report()` raises `RuntimeError` |
| Responsible disclosure only | 🟢 By design | Review queue gates all reports |

---

## Coverage Floors (from CLAUDE.md)

| Module | Floor | Current |
|---|---|---|
| `src/scope_enforcer/` | 85% | TBD — run `pytest --cov=src` |
| `src/triage/` | 80% | TBD |
| `src/h1_connector/` | 70% | TBD |
| `src/review_queue/` | 70% | TBD |
| `src/report_writer/` | 60% | TBD |

Run `pytest --cov=src --cov-report=term-missing` to get current numbers.

---

## Open Issues (to create as GitHub Issues)

Use the templates in `.github/ISSUE_TEMPLATE/` to create the following issues:

1. **Week 1** — `week1-h1-connector-db-schema.md`
2. **Week 2** — `week2-scope-enforcer.md`
3. **Week 3** — `week3-finding-importer.md`
4. **Week 4** — `week4-triage-layer.md`
5. **Week 5** — `week5-report-writer.md`
6. **Week 6** — `week6-cli-review-queue.md`
