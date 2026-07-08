"""
Shipment file domain model.

Represents the data loaded from a shipment JSON file.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ShipmentFile:
    """
    Shipment loaded from an input file.

    Attributes:
        carrier:
            Carrier name.

        statuses:
            Ordered raw carrier statuses.
    """

    carrier: str

    statuses: list[str]