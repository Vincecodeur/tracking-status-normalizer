from dataclasses import dataclass

from tracking_status_normalizer.domain.shipment_outcome import ShipmentOutcome
from tracking_status_normalizer.domain.status_category import StatusCategory


@dataclass(frozen=True)
class StatusDefinition:
    category: StatusCategory
    outcome: ShipmentOutcome
    terminal: bool