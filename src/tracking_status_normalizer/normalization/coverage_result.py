"""
Coverage analysis result.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CoverageResult:
    """
    Represents mapping catalog coverage statistics.
    """

    carrier: str

    total_statuses: int

    mapped_statuses: int

    unmapped_statuses: int

    coverage_percentage: float