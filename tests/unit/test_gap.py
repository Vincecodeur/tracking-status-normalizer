from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.gaps.gap import (
    Gap,
)
from tracking_status_normalizer.governance.gaps.gap_severity import (
    GapSeverity,
)


def test_create_gap():
    gap = Gap(
        capability=Capability.RETURNS,
        missing_status=CanonicalStatus.RETURN_DELIVERED,
        severity=GapSeverity.MEDIUM,
    )

    assert gap.capability == Capability.RETURNS
    assert gap.missing_status == CanonicalStatus.RETURN_DELIVERED
    assert gap.severity == GapSeverity.MEDIUM