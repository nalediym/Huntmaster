from hypothesis import given, settings
from hypothesis import strategies as st

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


# ---------------------------------------------------------------------------
# Hypothesis property-based tests
# ---------------------------------------------------------------------------

_safe_text = st.text(
    alphabet=st.characters(whitelist_categories=("Lu", "Ll", "Nd"), whitelist_characters="-._~"),
    min_size=1,
    max_size=30,
)

_hostname = st.builds(
    lambda sub, dom: f"{sub}.{dom}.com",
    st.text(alphabet="abcdefghijklmnopqrstuvwxyz0123456789", min_size=1, max_size=10),
    st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=2, max_size=10),
)

_url = _hostname.map(lambda h: f"https://{h}")


@given(_url)
@settings(max_examples=200)
def test_empty_scope_always_blocks(target):
    """With no scope assets, every target must be blocked."""
    enforcer = ScopeEnforcer([])
    result = enforcer.evaluate(target)
    assert result.decision != ScopeDecision.ALLOW


@given(_url)
@settings(max_examples=200)
def test_explicit_out_of_scope_never_allowed(target):
    """A target matching an out-of-scope asset must never be ALLOW."""
    enforcer = ScopeEnforcer([
        ScopeAsset(asset_type="URL", asset_value=target, eligible=False),
        ScopeAsset(asset_type="URL", asset_value=target, eligible=True),
    ])
    result = enforcer.evaluate(target)
    assert result.decision != ScopeDecision.ALLOW


@given(st.text(min_size=0, max_size=5))
@settings(max_examples=100)
def test_unsupported_asset_type_always_blocks(target):
    """An asset with an unsupported type must never allow any target."""
    enforcer = ScopeEnforcer([
        ScopeAsset(asset_type="UNKNOWN_TYPE_XYZ", asset_value="*", eligible=True)
    ])
    result = enforcer.evaluate(target if target else "https://x.com")
    assert result.decision != ScopeDecision.ALLOW


@given(_url)
@settings(max_examples=200)
def test_decision_is_never_none(target):
    """evaluate() must always return a valid decision, never raise."""
    enforcer = ScopeEnforcer([
        ScopeAsset(asset_type="URL", asset_value="https://app.example.com", eligible=True),
    ])
    result = enforcer.evaluate(target)
    assert result.decision in list(ScopeDecision)


@given(st.just(""))
def test_empty_target_is_blocked(target):
    """Empty string target must always be blocked."""
    enforcer = ScopeEnforcer([
        ScopeAsset(asset_type="WILDCARD", asset_value="*.example.com", eligible=True),
    ])
    result = enforcer.evaluate(target)
    assert result.decision != ScopeDecision.ALLOW
