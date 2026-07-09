"""
Maturity scoring.
"""

from tracking_status_normalizer.governance.coverage.coverage_level import (
    CoverageLevel,
)
from tracking_status_normalizer.governance.coverage.coverage_result import (
    CoverageResult,
)
from tracking_status_normalizer.governance.gaps.gap import (
    Gap,
)
from tracking_status_normalizer.governance.gaps.gap_severity import (
    GapSeverity,
)
from tracking_status_normalizer.governance.maturity.maturity_result import (
    MaturityResult,
)
from tracking_status_normalizer.governance.maturity.maturity_rules import (
    determine_maturity_level,
)
from tracking_status_normalizer.governance.readiness.readiness_level import (
    ReadinessLevel,
)
from tracking_status_normalizer.governance.readiness.readiness_result import (
    ReadinessResult,
)


def calculate_maturity(
    coverage_results: list[CoverageResult],
    readiness_result: ReadinessResult,
    gaps: list[Gap],
) -> MaturityResult:
    """
    Calculate catalog maturity score.
    """

    score = 100
    reasons: list[str] = []

    if readiness_result.level == ReadinessLevel.NO_GO:
        score -= 40
        reasons.append(
            "Catalog readiness is NO_GO."
        )

    elif readiness_result.level == ReadinessLevel.GO_WITH_RISKS:
        score -= 15
        reasons.append(
            "Catalog readiness is GO_WITH_RISKS."
        )

    for result in coverage_results:

        if result.level == CoverageLevel.NONE:
            score -= 10

        elif result.level == CoverageLevel.PARTIAL:
            score -= 5

    for gap in gaps:

        if gap.severity == GapSeverity.CRITICAL:
            score -= 10

        elif gap.severity == GapSeverity.MEDIUM:
            score -= 3

        elif gap.severity == GapSeverity.LOW:
            score -= 1

    score = max(0, min(score, 100))

    level = determine_maturity_level(score)

    return MaturityResult(
        score=score,
        level=level,
        reasons=reasons,
    )