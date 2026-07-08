from enum import Enum


class ShipmentOutcome(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    RETURNED = "RETURNED"
    FAILED = "FAILED"