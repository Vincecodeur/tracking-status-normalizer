"""
Carrier catalog domain model.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CarrierCatalog:
    """
    Represents a carrier mapping catalog.
    """

    carrier: str

    total_mappings: int