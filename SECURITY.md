# Security Posture

## Hard rules

- Only authorized HackerOne programs
- Never test out-of-scope assets
- Never store or exfiltrate real user data
- No credential stuffing
- Respect the program `policy` field
- Responsible disclosure only — no public posting before fix

## Credentials

All tokens are brokered via Agent Vault. Agents never see raw tokens directly.
The `.env` file is local only and must never be committed.

## Reporting vulnerabilities in Huntmaster itself

Report to the maintainer privately — do not open a public GitHub issue.
