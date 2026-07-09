"""
API error handling.

This module centralizes API error formatting for the FastAPI layer.

The goal is to return consistent and predictable error responses across
all endpoints.
"""

from enum import Enum
from typing import Any

from fastapi import Request
from fastapi.responses import JSONResponse


class APIErrorCode(str, Enum):
    """
    Stable API error codes.

    These codes are intended to be consumed by API clients.
    """

    MAPPING_FILE_NOT_FOUND = "MAPPING_FILE_NOT_FOUND"
    INVALID_MAPPING_FILE = "INVALID_MAPPING_FILE"
    UNKNOWN_CANONICAL_STATUS = "UNKNOWN_CANONICAL_STATUS"
    INVALID_REQUEST = "INVALID_REQUEST"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class APIError(Exception):
    """
    Custom API exception.

    This exception is raised explicitly by API endpoints when we want
    full control over the returned error code and message.
    """

    def __init__(
        self,
        code: APIErrorCode,
        message: str,
        status_code: int = 400,
        details: Any | None = None,
    ) -> None:
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details

        super().__init__(message)


def build_error_payload(
    code: APIErrorCode,
    message: str,
    details: Any | None = None,
) -> dict[str, Any]:
    """
    Build a standardized API error payload.

    Args:
        code:
            Stable API error code.

        message:
            Human-readable error message.

        details:
            Optional technical or validation details.

    Returns:
        Dictionary ready to be serialized as JSON.
    """

    return {
        "error": True,
        "code": code.value,
        "message": message,
        "details": details,
    }


async def api_error_handler(
    request: Request,
    exc: APIError,
) -> JSONResponse:
    """
    Handle explicitly raised APIError exceptions.
    """

    return JSONResponse(
        status_code=exc.status_code,
        content=build_error_payload(
            code=exc.code,
            message=exc.message,
            details=exc.details,
        ),
    )


async def file_not_found_handler(
    request: Request,
    exc: FileNotFoundError,
) -> JSONResponse:
    """
    Handle missing files.

    In the current API, this usually means the mapping file could not be found.
    """

    return JSONResponse(
        status_code=400,
        content=build_error_payload(
            code=APIErrorCode.MAPPING_FILE_NOT_FOUND,
            message=str(exc),
        ),
    )


async def value_error_handler(
    request: Request,
    exc: ValueError,
) -> JSONResponse:
    """
    Handle invalid business or input values.
    """

    return JSONResponse(
        status_code=400,
        content=build_error_payload(
            code=APIErrorCode.INVALID_REQUEST,
            message=str(exc),
        ),
    )