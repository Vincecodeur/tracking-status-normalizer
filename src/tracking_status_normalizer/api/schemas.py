"""
API schemas.

This module defines request and response models used by the FastAPI layer.
"""

from pydantic import BaseModel


class NormalizeStatusRequest(BaseModel):
    """
    Request body for single status normalization.

    Attributes:
        carrier:
            Carrier name.

        raw_status:
            Raw carrier status.

        mapping_file_path:
            Optional path to the mapping file.
            If not provided, the default project mapping file is used.
    """

    carrier: str
    raw_status: str
    mapping_file_path: str | None = None


class NormalizeStatusResponse(BaseModel):
    """
    Response returned after status normalization.
    """

    carrier: str
    raw_status: str
    canonical_status: str | None
    mapped: bool


class ValidateLifecycleRequest(BaseModel):
    """
    Request body for canonical lifecycle validation.

    Attributes:
        statuses:
            Ordered canonical statuses represented as strings.

    Example:
        [
            "IN_TRANSIT",
            "OUT_FOR_DELIVERY",
            "DELIVERED"
        ]
    """

    statuses: list[str]


class ValidateLifecycleResponse(BaseModel):
    """
    Response returned after lifecycle validation.
    """

    valid: bool
    reason: str | None


class ProcessShipmentRequest(BaseModel):
    """
    Request body for shipment processing.

    Attributes:
        carrier:
            Carrier name.

        statuses:
            Ordered raw carrier statuses.

        mapping_file_path:
            Optional path to the mapping file.
            If not provided, the default project mapping file is used.
    """

    carrier: str
    statuses: list[str]
    mapping_file_path: str | None = None


class ProcessShipmentResponse(BaseModel):
    """
    Response returned after shipment processing.
    """

    carrier: str

    validation: str
    validation_reason: str | None

    current_status: str
    outcome: str

    mapped_statuses: int
    unmapped_statuses: int