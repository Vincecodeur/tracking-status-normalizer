"""
Gap analysis.
"""

from tracking_status_normalizer.governance.coverage.coverage_result import (
    CoverageResult,
)
from tracking_status_normalizer.governance.gaps.gap import (
    Gap,
)
from tracking_status_normalizer.governance.gaps.gap_rules import (
    determine_gap_severity,
)


def analyze_gaps(
    coverage_results: list[CoverageResult],
) -> list[Gap]:
    """
    Analyze catalog gaps.

    Args:
        coverage_results:
            Coverage evaluation results.

    Returns:
        Identified gaps.
    """

    gaps: list[Gap] = []

    for result in coverage_results:

        severity = determine_gap_severity(
            capability=result.capability,
            coverage_level=result.level,
        )

        for missing_status in result.missing_statuses:

            gaps.append(
                Gap(
                    capability=result.capability,
                    missing_status=missing_status,
                    severity=severity,
                )
            )

    return gaps