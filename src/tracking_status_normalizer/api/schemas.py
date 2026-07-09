"""
API schemas.

This module defines request and response models used by the FastAPI layer.
"""

from typing import Any

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """
    Standard API error response.
    """

    error: bool
    code: str
    message: str
    details: Any | None = None


class NormalizeStatusRequest(BaseModel):
    """
    Request body for single status normalization.
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