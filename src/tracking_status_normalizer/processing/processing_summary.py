"""
Processing summary model.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ProcessingSummary:
    """
    Human-readable shipment processing summary.
    """

    carrier: str

    current_status: str

    outcome: str

    validation_status: str

    mapped_statuses: int

    unmapped_statuses: int