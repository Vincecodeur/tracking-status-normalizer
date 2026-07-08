"""
Defines all allowed transitions between canonical statuses.

This registry acts as the source of truth for shipment lifecycle validation.
"""

from tracking_status_normalizer.domain.canonical_status import CanonicalStatus


# Dictionary structure:
#
# CURRENT STATUS
#       ↓
# Allowed next statuses
#
ALLOWED_TRANSITIONS = {
    CanonicalStatus.PENDING: {
        CanonicalStatus.INFO_RECEIVED,
        CanonicalStatus.READY_FOR_PICKUP,
        CanonicalStatus.PICKED_UP,
    },

    CanonicalStatus.INFO_RECEIVED: {
        CanonicalStatus.READY_FOR_PICKUP,
        CanonicalStatus.PICKED_UP,
        CanonicalStatus.IN_TRANSIT,
    },

    CanonicalStatus.READY_FOR_PICKUP: {
        CanonicalStatus.PICKED_UP,
        CanonicalStatus.IN_TRANSIT,
    },

    CanonicalStatus.PICKED_UP: {
        CanonicalStatus.IN_TRANSIT,
        CanonicalStatus.ARRIVED_AT_FACILITY,
    },

    CanonicalStatus.IN_TRANSIT: {
        CanonicalStatus.ARRIVED_AT_FACILITY,
        CanonicalStatus.DEPARTED_FACILITY,
        CanonicalStatus.CUSTOMS_PROCESSING,
        CanonicalStatus.OUT_FOR_DELIVERY,
        CanonicalStatus.ARRIVED_AT_PICKUP_POINT,
        CanonicalStatus.EXCEPTION,
        CanonicalStatus.LOST,
        CanonicalStatus.DAMAGED,
        CanonicalStatus.HELD,
    },

    CanonicalStatus.OUT_FOR_DELIVERY: {
        CanonicalStatus.DELIVERED,
        CanonicalStatus.DELIVERY_ATTEMPT_FAILED,
        CanonicalStatus.RECIPIENT_UNAVAILABLE,
        CanonicalStatus.ADDRESS_ISSUE,
        CanonicalStatus.EXCEPTION,
    },

    CanonicalStatus.AVAILABLE_FOR_PICKUP: {
        CanonicalStatus.PICKED_UP_BY_CUSTOMER,
        CanonicalStatus.PICKUP_EXPIRED,
    },

    CanonicalStatus.PICKUP_EXPIRED: {
        CanonicalStatus.RETURN_INITIATED,
    },

    CanonicalStatus.DELIVERED: {
        # Option B validée :
        # livraison terminée, mais retour toujours possible
        CanonicalStatus.RETURN_INITIATED,
    },

    CanonicalStatus.RETURN_INITIATED: {
        CanonicalStatus.RETURN_IN_TRANSIT,
    },

    CanonicalStatus.RETURN_IN_TRANSIT: {
        CanonicalStatus.RETURN_DELIVERED,
    },
}