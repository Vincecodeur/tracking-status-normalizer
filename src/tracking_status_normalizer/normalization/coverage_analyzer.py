"""
Coverage analyzer.

Calculates mapping coverage for a collection of carrier statuses.
"""

from tracking_status_normalizer.normalization.coverage_result import (
    CoverageResult,
)
from tracking_status_normalizer.normalization.normalizer import (
    normalize,
)


def analyze_coverage(
    carrier: str,
    statuses: list[str],
    mapping_registry,
) -> CoverageResult:
    """
    Analyze mapping coverage for a given carrier.

    Args:
        carrier:
            Carrier name.

        statuses:
            List of raw carrier statuses.

        mapping_registry:
            Mapping registry loaded from the catalog.

    Returns:
            CoverageResult
    """

    total_statuses = len(statuses)

    mapped_statuses = 0

    for status in statuses:
        result = normalize(
            carrier,
            status,
            mapping_registry,
        )

        if result.mapped:
            mapped_statuses += 1

    unmapped_statuses = total_statuses - mapped_statuses

    coverage_percentage = 0.0

    if total_statuses > 0:
        coverage_percentage = (
            mapped_statuses / total_statuses
        ) * 100

    return CoverageResult(
        carrier=carrier,
        total_statuses=total_statuses,
        mapped_statuses=mapped_statuses,
        unmapped_statuses=unmapped_statuses,
        coverage_percentage=coverage_percentage,
    )