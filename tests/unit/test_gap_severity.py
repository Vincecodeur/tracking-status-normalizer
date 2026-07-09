from tracking_status_normalizer.governance.gaps.gap_severity import (
    GapSeverity,
)


def test_gap_severity_values():
    assert GapSeverity.CRITICAL.value == "CRITICAL"
    assert GapSeverity.MEDIUM.value == "MEDIUM"
    assert GapSeverity.LOW.value == "LOW"