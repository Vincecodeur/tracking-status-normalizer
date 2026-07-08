"""
Status registry.

This module defines the metadata attached to each canonical status.

The registry is the central source of truth for:
- status category
- shipment outcome
- terminal behavior
"""

from tracking_status_normalizer.domain.canonical_status import CanonicalStatus
from tracking_status_normalizer.domain.shipment_outcome import ShipmentOutcome
from tracking_status_normalizer.domain.status_category import StatusCategory
from tracking_status_normalizer.domain.status_definition import StatusDefinition


STATUS_REGISTRY: dict[CanonicalStatus, StatusDefinition] = {
    CanonicalStatus.PENDING: StatusDefinition(
        category=StatusCategory.PRE_SHIPMENT,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.INFO_RECEIVED: StatusDefinition(
        category=StatusCategory.PRE_SHIPMENT,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.READY_FOR_PICKUP: StatusDefinition(
        category=StatusCategory.PRE_SHIPMENT,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.PICKED_UP: StatusDefinition(
        category=StatusCategory.INBOUND,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.IN_TRANSIT: StatusDefinition(
        category=StatusCategory.TRANSIT,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.ARRIVED_AT_FACILITY: StatusDefinition(
        category=StatusCategory.TRANSIT,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.DEPARTED_FACILITY: StatusDefinition(
        category=StatusCategory.TRANSIT,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.CUSTOMS_PROCESSING: StatusDefinition(
        category=StatusCategory.TRANSIT,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.OUT_FOR_DELIVERY: StatusDefinition(
        category=StatusCategory.LAST_MILE,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.ARRIVED_AT_PICKUP_POINT: StatusDefinition(
        category=StatusCategory.LAST_MILE,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.DELIVERED_TO_PICKUP_POINT: StatusDefinition(
        category=StatusCategory.LAST_MILE,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.AVAILABLE_FOR_PICKUP: StatusDefinition(
        category=StatusCategory.LAST_MILE,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.DELIVERED: StatusDefinition(
        category=StatusCategory.DELIVERED,
        outcome=ShipmentOutcome.SUCCESS,
        terminal=False,
    ),
    CanonicalStatus.PICKED_UP_BY_CUSTOMER: StatusDefinition(
        category=StatusCategory.DELIVERED,
        outcome=ShipmentOutcome.SUCCESS,
        terminal=True,
    ),
    CanonicalStatus.DELIVERY_ATTEMPT_FAILED: StatusDefinition(
        category=StatusCategory.DELIVERY_EXCEPTION,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.ADDRESS_ISSUE: StatusDefinition(
        category=StatusCategory.DELIVERY_EXCEPTION,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.RECIPIENT_UNAVAILABLE: StatusDefinition(
        category=StatusCategory.DELIVERY_EXCEPTION,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.PICKUP_EXPIRED: StatusDefinition(
        category=StatusCategory.DELIVERY_EXCEPTION,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.RETURN_INITIATED: StatusDefinition(
        category=StatusCategory.RETURN,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.RETURN_IN_TRANSIT: StatusDefinition(
        category=StatusCategory.RETURN,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.RETURN_DELIVERED: StatusDefinition(
        category=StatusCategory.RETURN,
        outcome=ShipmentOutcome.RETURNED,
        terminal=True,
    ),
    CanonicalStatus.EXCEPTION: StatusDefinition(
        category=StatusCategory.EXCEPTION,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
    CanonicalStatus.LOST: StatusDefinition(
        category=StatusCategory.EXCEPTION,
        outcome=ShipmentOutcome.FAILED,
        terminal=True,
    ),
    CanonicalStatus.DAMAGED: StatusDefinition(
        category=StatusCategory.EXCEPTION,
        outcome=ShipmentOutcome.FAILED,
        terminal=True,
    ),
    CanonicalStatus.HELD: StatusDefinition(
        category=StatusCategory.EXCEPTION,
        outcome=ShipmentOutcome.IN_PROGRESS,
        terminal=False,
    ),
}