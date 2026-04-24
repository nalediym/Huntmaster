## Summary

Reflected XSS in search endpoint at `https://app.example.com/search` allows injection of arbitrary JavaScript into
the response via the `q` parameter. An attacker who tricks a user into visiting a crafted URL can steal session
cookies or perform actions on behalf of the victim.

## Vulnerability Details

- Type: Reflected Cross-Site Scripting (XSS)
- CWE: CWE-79
- CVSS Score: 6.1 (Medium)
- Affected Asset: https://app.example.com/search

## Steps to Reproduce

1. Confirm you are authorized to test `app.example.com` under the Example Corp program.
2. Send the following request:

```
GET /search?q=<script>alert(document.cookie)</script> HTTP/1.1
Host: app.example.com
```

3. Observe that the injected script executes in the browser context.

## Proof of Concept

```text
GET /search?q=<script>alert(document.cookie)</script> HTTP/1.1
Host: app.example.com
```

## Impact

A remote attacker can execute arbitrary JavaScript in the victim's browser session, leading to session hijacking,
credential theft, or account takeover.

## Remediation

- HTML-encode all user-supplied input before reflecting it in the response.
- Apply a Content Security Policy (CSP) that blocks inline scripts.
- Validate and reject input containing `<script>` or event handler attributes at the WAF layer.

## Supporting Evidence

Screenshot shows alert box firing with session cookie value in Chrome 124 on an unmodified session.
