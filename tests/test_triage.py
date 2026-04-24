from huntmaster.models import ScopeAsset
from huntmaster.scope_enforcer import ScopeEnforcer
from huntmaster.triage import triage_finding


def test_triage_approves_valid_in_scope_finding():
    enforcer = ScopeEnforcer([
        ScopeAsset(asset_type="URL", asset_value="https://app.example.com/search", eligible=True)
    ])
    finding = {
        "asset": "https://app.example.com/search",
        "cvss_score": 4.3,
        "validated": True,
    }

    result = triage_finding(finding, enforcer)

    assert result["triage_status"] == "approved"


def test_triage_rejects_out_of_scope_finding():
    enforcer = ScopeEnforcer([
        ScopeAsset(asset_type="URL", asset_value="https://app.example.com", eligible=True)
    ])
    finding = {
        "asset": "https://evil.example.net",
        "cvss_score": 9.0,
        "validated": True,
    }

    result = triage_finding(finding, enforcer)

    assert result["triage_status"] == "rejected"
