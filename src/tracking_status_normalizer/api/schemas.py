"""
API schemas.

This module defines request and response models used by the FastAPI layer.
"""

from pydantic import BaseModel


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