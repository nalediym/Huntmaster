# Architecture

## Design goals

Huntmaster is designed around one central safety invariant:

> No target reaches a testing or report-generation path until it passes explicit scope validation.

## Components

```text
HackerOne Connector
  ↓
Program + Scope Store
  ↓
Scope Enforcer
  ↓
Manual Finding Import
  ↓
Triage Layer
  ↓
Report Writer
  ↓
Human Review Queue
```

## Component responsibilities

### HackerOne Connector

Reads program metadata and structured scope. In v0.1, this connector is read-only.

### Program + Scope Store

Persists normalized program and scope records.

### Scope Enforcer

Evaluates whether a target is clearly allowed, denied, or ambiguous.

Decision states:

- `ALLOW`
- `BLOCK_OUT_OF_SCOPE`
- `BLOCK_AMBIGUOUS`
- `BLOCK_UNSUPPORTED_ASSET_TYPE`
- `BLOCK_POLICY_RESTRICTED`

### Manual Finding Import

Accepts structured JSON from external tools. The project does not ship exploit modules or automated attack workflows.

### Triage Layer

Checks evidence quality, scope, duplicate risk, severity threshold, and policy compliance.

### Report Writer

Produces Markdown drafts from validated findings.

### Review Queue

Keeps Naledi in control. No report is submitted automatically.

## State model

```text
program -> scope[]
program -> finding[]
finding -> report?
finding -> skill_log[]
```

## Deployment path

v0.1 can run locally as a Python CLI with SQLite. Future deployment can move the same schema to Cloudflare D1 and use Cloudflare Workers for orchestration.
