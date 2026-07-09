from tracking_status_normalizer.governance.maturity.maturity_level import (
    MaturityLevel,
)
from tracking_status_normalizer.governance.maturity.maturity_result import (
    MaturityResult,
)


def test_create_maturity_result():
    result = MaturityResult(
        score=85,
        level=MaturityLevel.MATURE,
        reasons=["Example reason"],
    )

    assert result.score == 85
    assert result.level == MaturityLevel.MATURE
    assert result.reasons == ["Example reason"]