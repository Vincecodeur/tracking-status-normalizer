"""
Tests for readiness result model.
"""

from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.readiness.readiness_level import (
    ReadinessLevel,
)
from tracking_status_normalizer.governance.readiness.readiness_result import (
    ReadinessResult,
)


def test_create_readiness_result():
    result = ReadinessResult(
        level=ReadinessLevel.NO_GO,
        blocking_capabilities=[
            Capability.DIRECT_DELIVERY,
        ],
        risk_capabilities=[
            Capability.RETURNS,
        ],
        reasons=[
            "DIRECT_DELIVERY is PARTIAL.",
            "RETURNS is NONE.",
        ],
    )

    assert result.level == ReadinessLevel.NO_GO

    assert result.blocking_capabilities == [
        Capability.DIRECT_DELIVERY,
    ]

    assert result.risk_capabilities == [
        Capability.RETURNS,
    ]

    assert result.reasons == [
        "DIRECT_DELIVERY is PARTIAL.",
        "RETURNS is NONE.",
    ]