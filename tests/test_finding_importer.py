import pytest

from huntmaster.finding_importer import import_finding, FindingImportError


VALID_FINDING = {
    "program_id": "example-corp",
    "title": "XSS in search",
    "asset": "https://app.example.com/search",
    "cvss_score": 6.1,
    "validated": True,
}


def test_import_valid_finding():
    result = import_finding(VALID_FINDING)
    assert result["program_id"] == "example-corp"
    assert result["cvss_score"] == 6.1
    assert result["validated"] is True


def test_import_missing_required_field_raises():
    bad = {k: v for k, v in VALID_FINDING.items() if k != "title"}
    with pytest.raises(FindingImportError, match="title"):
        import_finding(bad)


def test_import_invalid_cvss_type_raises():
    bad = {**VALID_FINDING, "cvss_score": "high"}
    with pytest.raises(FindingImportError, match="cvss_score"):
        import_finding(bad)


def test_import_cvss_out_of_range_raises():
    bad = {**VALID_FINDING, "cvss_score": 11.0}
    with pytest.raises(FindingImportError, match="0.0"):
        import_finding(bad)


def test_import_optional_fields_default_to_none():
    minimal = {
        "program_id": "p",
        "title": "t",
        "asset": "https://app.example.com",
        "cvss_score": 5.0,
    }
    result = import_finding(minimal)
    assert result["cwe_id"] is None
    assert result["poc"] is None
    assert result["validated"] is False
