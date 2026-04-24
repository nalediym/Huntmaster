def draft_report(finding: dict) -> str:
    """Create a HackerOne-style Markdown draft from a validated finding."""

    title = finding.get("title", "Untitled finding")
    cwe = finding.get("cwe_id", "Unknown")
    cvss = finding.get("cvss_score", "Unknown")
    asset = finding.get("asset", "Unknown")
    poc = finding.get("poc", "No proof of concept provided.")
    evidence = finding.get("evidence", "No supporting evidence provided.")

    return f"""## Summary

{title}

## Vulnerability Details

- Type: {title}
- CWE: {cwe}
- CVSS Score: {cvss}
- Affected Asset: {asset}

## Steps to Reproduce

1. Confirm you are authorized to test the affected asset.
2. Reproduce the issue using the sanitized proof of concept below.
3. Observe the behavior described in the supporting evidence.

## Proof of Concept

```text
{poc}
```

## Impact

Impact should be reviewed by a human and limited to what the evidence proves.

## Remediation

Validate inputs, enforce least privilege, and apply the framework-specific fix for the vulnerability class.

## Supporting Evidence

{evidence}
"""
