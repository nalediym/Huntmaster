from huntmaster.report_writer.markdown import draft_report


def test_draft_report_contains_title():
    finding = {
        "title": "SQL Injection in login form",
        "asset": "https://app.example.com/login",
        "cvss_score": 9.8,
        "cwe_id": "CWE-89",
        "poc": "' OR '1'='1",
        "evidence": "Database error message returned.",
    }
    report = draft_report(finding)
    assert "SQL Injection in login form" in report


def test_draft_report_contains_asset():
    finding = {
        "title": "IDOR on user profile",
        "asset": "https://app.example.com/users/42",
        "cvss_score": 5.3,
    }
    report = draft_report(finding)
    assert "https://app.example.com/users/42" in report


def test_draft_report_default_poc_placeholder():
    finding = {
        "title": "Test",
        "asset": "https://app.example.com",
        "cvss_score": 4.0,
    }
    report = draft_report(finding)
    assert "No proof of concept provided." in report
