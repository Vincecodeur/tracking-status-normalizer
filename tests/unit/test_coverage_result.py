from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.coverage.coverage_level import (
    CoverageLevel,
)
from tracking_status_normalizer.governance.coverage.coverage_result import (
    CoverageResult,
)


def test_create_coverage_result():
    result = CoverageResult(
        capability=Capability.RETURNS,
        level=CoverageLevel.PARTIAL,
        required_statuses=3,
        covered_statuses=2,
        missing_statuses=[
            CanonicalStatus.RETURN_DELIVERED,
        ],
    )

    assert result.capability == Capability.RETURNS
    assert result.level == CoverageLevel.PARTIAL
    assert result.required_statuses == 3
    assert result.covered_statuses == 2