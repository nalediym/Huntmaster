# Roadmap

## Milestone: v0.1 — Human-Gated MVP

### Week 1: HackerOne connector + DB schema

- [ ] Create database schema
- [ ] Add environment variable loading
- [ ] Add read-only HackerOne client stub
- [ ] Add program/scope normalization models
- [ ] Add tests for stored program records

### Week 2: Scope Enforcer

- [ ] Implement exact URL matching
- [ ] Implement wildcard domain matching
- [ ] Implement out-of-scope deny-list priority
- [ ] Add ambiguous-scope blocking
- [ ] Add audit logs for all decisions

### Week 3: Manual JSON import

- [ ] Define finding input schema
- [ ] Parse sample finding JSON
- [ ] Validate findings against scope before storage
- [ ] Reject unsupported or incomplete findings
- [ ] Add tests for malformed JSON

### Week 4: Triage layer

- [ ] Add CVSS threshold checks
- [ ] Add duplicate-risk check against local history
- [ ] Add evidence-quality checklist
- [ ] Add policy compliance check
- [ ] Store triage reason

### Week 5: Report writer

- [ ] Add Markdown report template
- [ ] Add prompt template for external report writer
- [ ] Generate report drafts from validated findings
- [ ] Add tests for required report sections

### Week 6: CLI review queue

- [ ] List pending draft reports
- [ ] View report details
- [ ] Mark approved, edited, or rejected
- [ ] Log rejection reasons
- [ ] Prepare first authorized live workflow

## Future: v0.2

- Cloudflare Workers orchestration
- Cloudflare D1 deployment
- Durable Object per program session
- Outcome tracking
- Program scoring
- Learning logs

## Future: v0.3

- Dashboard
- Duplicate detection improvements
- Rate-limit-aware sync
- Program policy parser
- Safer integration with external testing tools
