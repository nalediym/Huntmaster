from huntmaster.models import ScopeAsset, ScopeDecision
from huntmaster.scope_enforcer import ScopeEnforcer


def test_allows_exact_in_scope_url():
    enforcer = ScopeEnforcer([
        ScopeAsset(asset_type="URL", asset_value="https://app.example.com", eligible=True)
    ])

    result = enforcer.evaluate("https://app.example.com")

    assert result.decision == ScopeDecision.ALLOW


def test_blocks_explicit_out_of_scope_before_allow():
    enforcer = ScopeEnforcer([
        ScopeAsset(asset_type="WILDCARD", asset_value="*.example.com", eligible=True),
        ScopeAsset(asset_type="URL", asset_value="https://admin.example.com", eligible=False),
    ])

    result = enforcer.evaluate("https://admin.example.com")

    assert result.decision == ScopeDecision.BLOCK_OUT_OF_SCOPE


def test_blocks_ambiguous_target():
    enforcer = ScopeEnforcer([
        ScopeAsset(asset_type="URL", asset_value="https://app.example.com", eligible=True)
    ])

    result = enforcer.evaluate("https://unknown.example.com")

    assert result.decision == ScopeDecision.BLOCK_AMBIGUOUS
