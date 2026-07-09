"""
Operational capability definitions.

This module defines all logistics capabilities that can be evaluated
by the Governance Layer.

Capabilities describe what logistics flows a carrier catalog is able
to represent through canonical statuses.
"""

from enum import Enum


class Capability(str, Enum):
    """
    Logistics capabilities supported by the governance model.
    """

    DIRECT_DELIVERY = "DIRECT_DELIVERY"

    PUDO = "PUDO"

    LOCKER = "LOCKER"

    OUT_OF_HOME_DELIVERY = "OUT_OF_HOME_DELIVERY"

    RETURNS = "RETURNS"

    CUSTOMS = "CUSTOMS"

    EXCEPTION_MANAGEMENT = "EXCEPTION_MANAGEMENT"