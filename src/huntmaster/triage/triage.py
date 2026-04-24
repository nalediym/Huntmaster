from huntmaster.models import ScopeDecision
from huntmaster.scope_enforcer import ScopeEnforcer


def triage_finding(finding: dict, scope_enforcer: ScopeEnforcer, cvss_minimum: float = 4.0) -> dict:
    """Triage a structured finding.

    This function does not validate exploitability. It checks structured metadata and scope.
    """

    asset = finding.get("asset", "")
    scope_eval = scope_enforcer.evaluate(asset)

    if scope_eval.decision != ScopeDecision.ALLOW:
        return {
            "triage_status": "rejected",
            "reason": scope_eval.reason,
            "scope_decision": scope_eval.decision.value,
            "next_action": "reject",
        }

    score = float(finding.get("cvss_score") or 0)
    if score < cvss_minimum:
        return {
            "triage_status": "rejected",
            "reason": f"CVSS score {score} is below threshold {cvss_minimum}.",
            "scope_decision": scope_eval.decision.value,
            "next_action": "reject",
        }

    if not finding.get("validated"):
        return {
            "triage_status": "needs_human_review",
            "reason": "Finding is not marked validated.",
            "scope_decision": scope_eval.decision.value,
            "next_action": "request_more_evidence",
        }

    return {
        "triage_status": "approved",
        "reason": "Finding passed basic scope, CVSS, and validation checks.",
        "scope_decision": scope_eval.decision.value,
        "next_action": "draft_report",
    }
