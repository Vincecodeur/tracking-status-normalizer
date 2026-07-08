"""
Unmapped report models.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class UnmappedStatus:
    """
    Represents an unmapped carrier status.
    """

    carrier: str
    raw_status: str
    occurrences: int


@dataclass(frozen=True)
class UnmappedReport:
    """
    Represents a collection of unmapped statuses.
    """

    total_unknown_statuses: int

    statuses: list[UnmappedStatus]