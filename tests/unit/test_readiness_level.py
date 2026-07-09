"""
Tests for readiness level definitions.
"""

from tracking_status_normalizer.governance.readiness.readiness_level import (
    ReadinessLevel,
)


def test_readiness_levels():
    assert ReadinessLevel.GO.value == "GO"

    assert (
        ReadinessLevel.GO_WITH_RISKS.value
        == "GO_WITH_RISKS"
    )

    assert ReadinessLevel.NO_GO.value == "NO_GO"