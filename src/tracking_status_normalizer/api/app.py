"""
FastAPI application.

This module exposes the Tracking Status Normalizer engine through HTTP endpoints.
"""

from fastapi import FastAPI, HTTPException

from tracking_status_normalizer.api.schemas import (
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
    version="0.4.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    """
    Health check endpoint.

    Returns:
        Basic API health status.
    """

    return {
        "status": "ok",
    }


@app.post(
    "/normalize",
    response_model=NormalizeStatusResponse,
)
def normalize_status_endpoint(
    request: NormalizeStatusRequest,
) -> NormalizeStatusResponse:
    """
    Normalize a single raw carrier status.

    This endpoint converts one carrier-specific status into a canonical status.
    """

    mapping_file_path = (
        request.mapping_file_path
        or DEFAULT_MAPPING_FILE
    )

    try:
        mapping_registry = load_mapping_file(
            mapping_file_path
        )

        result = normalize(
            carrier=request.carrier,
            raw_status=request.raw_status,
            mapping_registry=mapping_registry,
        )

    except FileNotFoundError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error

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
)
def validate_lifecycle_endpoint(
    request: ValidateLifecycleRequest,
) -> ValidateLifecycleResponse:
    """
    Validate a lifecycle made of canonical statuses.

    The input statuses must already be canonical status values.
    """

    try:
        canonical_statuses = [
            CanonicalStatus(status)
            for status in request.statuses
        ]

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail="Unknown canonical status in request.",
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

    try:
        mapping_registry = load_mapping_file(
            mapping_file_path
        )

        result = process_shipment(
            carrier=request.carrier,
            statuses=request.statuses,
            mapping_registry=mapping_registry,
        )

    except FileNotFoundError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error

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