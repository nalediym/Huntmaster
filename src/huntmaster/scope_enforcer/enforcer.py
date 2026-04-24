from urllib.parse import urlparse

from huntmaster.models import ScopeAsset, ScopeDecision, ScopeEvaluation


SUPPORTED_ASSET_TYPES = {"URL", "WILDCARD", "CIDR", "ANDROID_APP", "IOS_APP", "OTHER"}


class ScopeEnforcer:
    """Conservative scope checker.

    Safety invariant: if the checker cannot prove that a target is allowed, it blocks.
    """

    def __init__(self, assets: list[ScopeAsset]) -> None:
        self.assets = assets

    def evaluate(self, target: str) -> ScopeEvaluation:
        if not target or not isinstance(target, str):
            return ScopeEvaluation(
                target=target,
                decision=ScopeDecision.BLOCK_AMBIGUOUS,
                reason="Target is empty or invalid.",
            )

        for asset in self.assets:
            if asset.asset_type not in SUPPORTED_ASSET_TYPES:
                return ScopeEvaluation(
                    target=target,
                    decision=ScopeDecision.BLOCK_UNSUPPORTED_ASSET_TYPE,
                    reason=f"Unsupported asset type: {asset.asset_type}",
                )

        for asset in [asset for asset in self.assets if not asset.eligible]:
            if self._matches(asset, target):
                return ScopeEvaluation(
                    target=target,
                    decision=ScopeDecision.BLOCK_OUT_OF_SCOPE,
                    reason=f"Target matches explicit out-of-scope asset: {asset.asset_value}",
                )

        for asset in [asset for asset in self.assets if asset.eligible]:
            if self._matches(asset, target):
                return ScopeEvaluation(
                    target=target,
                    decision=ScopeDecision.ALLOW,
                    reason=f"Target matches in-scope asset: {asset.asset_value}",
                )

        return ScopeEvaluation(
            target=target,
            decision=ScopeDecision.BLOCK_AMBIGUOUS,
            reason="No explicit in-scope match found.",
        )

    def _matches(self, asset: ScopeAsset, target: str) -> bool:
        if asset.asset_type == "URL":
            return self._normalize_url(asset.asset_value) == self._normalize_url(target)

        if asset.asset_type == "WILDCARD":
            return self._matches_wildcard(asset.asset_value, target)

        # v0.1 blocks complex asset types until explicit handlers exist.
        return False

    def _normalize_url(self, value: str) -> str:
        parsed = urlparse(value)
        scheme = parsed.scheme.lower()
        netloc = parsed.netloc.lower()
        path = parsed.path.rstrip("/")
        return f"{scheme}://{netloc}{path}"

    def _matches_wildcard(self, pattern: str, target: str) -> bool:
        parsed = urlparse(target)
        host = parsed.netloc.lower() if parsed.netloc else target.lower()
        pattern = pattern.lower().strip()

        if not pattern.startswith("*."):
            return False

        suffix = pattern[1:]
        return host.endswith(suffix) and host != suffix.lstrip(".")
