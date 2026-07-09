"""
FastAPI application.

This module exposes the Tracking Status Normalizer engine through HTTP endpoints.
"""

from fastapi import FastAPI

from tracking_status_normalizer.api.errors import (
    APIError,
    APIErrorCode,
    api_error_handler,
    file_not_found_handler,
    value_error_handler,
)
from tracking_status_normalizer.api.schemas import (
    ErrorResponse,
    NormalizeStatusRequest,
    NormalizeStatusResponse,
    ProcessShipmentRequest,
    ProcessShipmentResponse,
    ValidateLifecycleRequest,
    ValidateLifecycleResponse,
)
from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.normalization.mapping_loader import (
    load_mapping_file,
)
from tracking_status_normalizer.normalization.normalizer import (
    normalize,
)
from tracking_status_normalizer.processing.shipment_processor import (
    process_shipment,
)
from tracking_status_normalizer.validation.lifecycle_validator import (
    validate_lifecycle,
)


DEFAULT_MAPPING_FILE = "data/mappings/carrier_status_mapping.json"


app = FastAPI(
    title="Tracking Status Normalizer API",
    description=(
        "API for carrier status normalization, shipment lifecycle validation, "
        "and shipment processing."
    ),
    version="0.5.0",
)


# Centralized API exception handlers.
app.add_exception_handler(
    APIError,
    api_error_handler,
)

app.add_exception_handler(
    FileNotFoundError,
    file_not_found_handler,
)

app.add_exception_handler(
    ValueError,
    value_error_handler,
)


ERROR_RESPONSES = {
    400: {
        "model": ErrorResponse,
        "description": "Business or request error.",
    }
}


@app.get("/health")
def health_check() -> dict[str, str]:
    """
    Health check endpoint.
    """

    return {
        "status": "ok",
    }


@app.post(
    "/normalize",
    response_model=NormalizeStatusResponse,
    responses=ERROR_RESPONSES,
)
def normalize_status_endpoint(
    request: NormalizeStatusRequest,
) -> NormalizeStatusResponse:
    """
    Normalize a single raw carrier status.
    """

    mapping_file_path = (
        request.mapping_file_path
        or DEFAULT_MAPPING_FILE
    )

    mapping_registry = load_mapping_file(
        mapping_file_path
    )

    result = normalize(
        carrier=request.carrier,
        raw_status=request.raw_status,
        mapping_registry=mapping_registry,
    )

    canonical_status = (
        result.canonical_status.value
        if result.canonical_status is not None
        else None
    )

    return NormalizeStatusResponse(
        carrier=result.carrier,
        raw_status=result.raw_status,
        canonical_status=canonical_status,
        mapped=result.mapped,
    )


@app.post(
    "/validate",
    response_model=ValidateLifecycleResponse,
    responses=ERROR_RESPONSES,
)
def validate_lifecycle_endpoint(
    request: ValidateLifecycleRequest,
) -> ValidateLifecycleResponse:
    """
    Validate a lifecycle made of canonical statuses.
    """

    try:
        canonical_statuses = [
            CanonicalStatus(status)
            for status in request.statuses
        ]

    except ValueError as error:
        raise APIError(
            code=APIErrorCode.UNKNOWN_CANONICAL_STATUS,
            message="Unknown canonical status in request.",
            status_code=400,
            details={
                "statuses": request.statuses,
            },
        ) from error

    result = validate_lifecycle(
        canonical_statuses
    )

    return ValidateLifecycleResponse(
        valid=result.valid,
        reason=result.reason,
    )


@app.post(
    "/process",
    response_model=ProcessShipmentResponse,
    responses=ERROR_RESPONSES,
)
def process_shipment_endpoint(
    request: ProcessShipmentRequest,
) -> ProcessShipmentResponse:
    """
    Process a shipment lifecycle from raw carrier statuses.

    This endpoint orchestrates:
    - mapping loading
    - status normalization
    - lifecycle validation
    - lifecycle analysis
    """

    mapping_file_path = (
        request.mapping_file_path
        or DEFAULT_MAPPING_FILE
    )

    mapping_registry = load_mapping_file(
        mapping_file_path
    )

    result = process_shipment(
        carrier=request.carrier,
        statuses=request.statuses,
        mapping_registry=mapping_registry,
    )

    validation_status = (
        "VALID"
        if result.validation.valid
        else "INVALID"
    )

    return ProcessShipmentResponse(
        carrier=request.carrier,
        validation=validation_status,
        validation_reason=result.validation.reason,
        current_status=result.lifecycle.current_status.value,
        outcome=result.lifecycle.current_outcome.value,
        mapped_statuses=result.mapped_statuses,
        unmapped_statuses=result.unmapped_statuses,
    )