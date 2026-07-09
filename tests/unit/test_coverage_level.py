from tracking_status_normalizer.governance.coverage.coverage_level import (
    CoverageLevel,
)


def test_coverage_levels():
    assert CoverageLevel.FULL.value == "FULL"
    assert CoverageLevel.PARTIAL.value == "PARTIAL"
    assert CoverageLevel.NONE.value == "NONE"