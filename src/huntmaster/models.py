from dataclasses import dataclass
from enum import Enum


class ScopeDecision(str, Enum):
    ALLOW = "ALLOW"
    BLOCK_OUT_OF_SCOPE = "BLOCK_OUT_OF_SCOPE"
    BLOCK_AMBIGUOUS = "BLOCK_AMBIGUOUS"
    BLOCK_UNSUPPORTED_ASSET_TYPE = "BLOCK_UNSUPPORTED_ASSET_TYPE"
    BLOCK_POLICY_RESTRICTED = "BLOCK_POLICY_RESTRICTED"


@dataclass(frozen=True)
class ScopeAsset:
    asset_type: str
    asset_value: str
    eligible: bool
    instruction: str | None = None


@dataclass(frozen=True)
class ScopeEvaluation:
    target: str
    decision: ScopeDecision
    reason: str
