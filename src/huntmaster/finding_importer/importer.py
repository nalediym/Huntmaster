"""Manual finding importer.

Consumes structured JSON findings from an external authorized testing process.
v0.1 does not trigger autonomous scanning — all findings must be imported manually.
"""

from __future__ import annotations

REQUIRED_FIELDS = {"program_id", "title", "asset", "cvss_score"}


class FindingImportError(ValueError):
    pass


def import_finding(raw: dict) -> dict:
    """Validate and normalise a raw finding dict.

    Raises FindingImportError if required fields are missing or invalid.
    Returns a clean finding dict ready for triage.
    """
    missing = REQUIRED_FIELDS - raw.keys()
    if missing:
        raise FindingImportError(f"Missing required fields: {sorted(missing)}")

    try:
        cvss = float(raw["cvss_score"])
    except (TypeError, ValueError) as exc:
        raise FindingImportError(f"Invalid cvss_score: {raw['cvss_score']!r}") from exc

    if not (0.0 <= cvss <= 10.0):
        raise FindingImportError(f"cvss_score must be 0.0–10.0, got {cvss}")

    return {
        "program_id": str(raw["program_id"]),
        "title": str(raw["title"]),
        "asset": str(raw["asset"]),
        "cvss_score": cvss,
        "cwe_id": raw.get("cwe_id"),
        "poc": raw.get("poc"),
        "evidence": raw.get("evidence"),
        "validated": bool(raw.get("validated", False)),
        "apex_output": raw.get("apex_output"),
    }
