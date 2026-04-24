# Ethics and Safety Policy

Huntmaster is for authorized security research only.

## Non-negotiable rules

1. **Authorized programs only**  
   Only use this project with programs where you are an authorized participant.

2. **Explicit scope only**  
   Never test assets outside the program's published scope.

3. **Ambiguous means blocked**  
   If the project cannot prove that an asset is in scope, it must block the action and request human review.

4. **No real-user data collection**  
   Do not store, reproduce, exfiltrate, or share real user data. If a proof of concept reveals sensitive data, stop immediately and redact.

5. **Respect program policy**  
   Some programs prohibit automated testing, high-volume requests, social engineering, denial of service, or specific vulnerability classes. Those rules override all project behavior.

6. **No autonomous submission**  
   Reports require explicit human approval.

7. **Responsible disclosure only**  
   Findings go to the affected program through the approved disclosure channel.

## Public repository boundary

This public repository should not include:

- exploit modules
- credential stuffing workflows
- stealth or evasion logic
- bypass techniques
- payload libraries
- destructive testing
- automated submission scripts

## Acceptable v0.1 work

- scope parsing
- allow-list / deny-list validation
- policy checks
- finding JSON parsing
- severity and duplicate-risk triage
- report drafting
- audit logging
- human review workflow
