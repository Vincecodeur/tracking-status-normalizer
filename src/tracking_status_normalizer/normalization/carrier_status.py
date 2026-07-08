"""
Carrier status model.

Represents a raw tracking status received from a carrier.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CarrierStatus:
    """
    Raw carrier tracking status.

    Example:
        carrier = "DHL"
        raw_value = "Shipment delivered"
    """

    carrier: str
    raw_value: str