# Tracking Status Normalizer

Current version: 0.5.0

A Python platform for carrier status normalization, shipment lifecycle validation, shipment processing, and API-based tracking analytics.

---

# Overview

Carriers use different tracking vocabularies.

Examples:

| Carrier         | Raw Status            |
| --------------- | --------------------- |
| DHL             | Shipment delivered    |
| UPS             | Delivered             |
| Colissimo       | Votre colis est livré |
| Amazon Shipping | Package delivered     |

The Tracking Status Normalizer converts heterogeneous carrier statuses into a common canonical tracking language.

Example:

```text
Shipment delivered
Delivered
Votre colis est livré
Package delivered

        ↓

DELIVERED
```

The project provides:

- Canonical shipment tracking taxonomy
- Carrier status normalization
- Shipment lifecycle validation
- Shipment lifecycle analysis
- Shipment processing engine
- Catalog governance tools
- Command Line Interface
- FastAPI REST API
- Structured API error handling
- GitHub Actions CI
- Python package distribution support

---

# Core Capabilities

## 1. Canonical Tracking Taxonomy

The project defines a carrier-neutral tracking status model.

### Canonical Statuses

```text
PENDING

INFO_RECEIVED
READY_FOR_PICKUP

PICKED_UP

IN_TRANSIT
ARRIVED_AT_FACILITY
DEPARTED_FACILITY
CUSTOMS_PROCESSING

OUT_FOR_DELIVERY

ARRIVED_AT_PICKUP_POINT
DELIVERED_TO_PICKUP_POINT
AVAILABLE_FOR_PICKUP

DELIVERED
PICKED_UP_BY_CUSTOMER

DELIVERY_ATTEMPT_FAILED
ADDRESS_ISSUE
RECIPIENT_UNAVAILABLE
PICKUP_EXPIRED

RETURN_INITIATED
RETURN_IN_TRANSIT
RETURN_DELIVERED

EXCEPTION
LOST
DAMAGED
HELD
```

### Status Categories

```text
PRE_SHIPMENT
INBOUND
TRANSIT
LAST_MILE
DELIVERED
DELIVERY_EXCEPTION
RETURN
EXCEPTION
```

### Shipment Outcomes

```text
IN_PROGRESS
SUCCESS
RETURNED
FAILED
```

---

## 2. Status Normalization

The normalization engine converts carrier-specific statuses into canonical statuses.

Example:

```python
normalize(
    carrier="DHL",
    raw_status="Shipment delivered",
    mapping_registry=registry,
)
```

Result:

```python
NormalizationResult(
    carrier="DHL",
    raw_status="Shipment delivered",
    canonical_status=CanonicalStatus.DELIVERED,
    mapped=True,
)
```

---

## 3. Lifecycle Validation

The validation engine checks whether a shipment status sequence follows valid lifecycle transitions.

Valid lifecycle:

```text
IN_TRANSIT
↓
OUT_FOR_DELIVERY
↓
DELIVERED
```

Invalid lifecycle:

```text
DELIVERED
↓
IN_TRANSIT
```

---

## 4. Lifecycle Analysis

The analysis engine calculates:

- Current status
- Current category
- Shipment outcome
- Terminal status flag
- Exception presence
- Return flow presence

---

## 5. Shipment Processing

The shipment processor orchestrates the complete workflow.

```text
Raw Carrier Statuses
        ↓
Text Normalization
        ↓
Carrier Mapping
        ↓
Canonical Statuses
        ↓
Lifecycle Validation
        ↓
Lifecycle Analysis
        ↓
Shipment Result
```

---

## 6. Catalog Governance

The project includes catalog quality and governance tools:

- Unknown status detection
- Coverage analysis
- Catalog analysis
- Unmapped status reporting

These capabilities help identify missing mappings and improve mapping catalog quality over time.

---

# Supported Logistics Flows

The taxonomy supports:

- Home delivery
- Business delivery
- Pickup point delivery
- Locker delivery
- Customer collection
- Delivery failures
- Expired pickup windows
- Automatic returns
- Customer-initiated returns
- Customs processing
- Shipment loss
- Damaged shipments
- Operational exceptions

---

# Project Architecture

```text
src/
└── tracking_status_normalizer/
    │
    ├── api/
    ├── analysis/
    ├── catalog/
    ├── cli/
    ├── domain/
    ├── io/
    ├── normalization/
    ├── processing/
    └── validation/
```

## api/

FastAPI application layer.

Exposes the engine through HTTP endpoints.

## analysis/

Lifecycle analysis engine.

Computes business summaries from canonical status lifecycles.

## catalog/

Catalog quality and governance.

Includes coverage analysis, catalog statistics, and unmapped status reporting.

## cli/

Command line interface.

Provides terminal access to the shipment processing engine.

## domain/

Core business model.

Includes canonical statuses, categories, outcomes, status definitions, and transition rules.

## io/

Input file loading.

Currently supports shipment JSON files.

## normalization/

Carrier status normalization.

Includes text normalization, mapping loading, normalization result objects, and unknown status detection.

## processing/

End-to-end shipment processing engine.

Combines normalization, validation, and lifecycle analysis.

## validation/

Lifecycle validation engine.

Validates canonical status transitions and full shipment lifecycles.

---

# Installation

## Development Installation

```bash
git clone https://github.com/Vincecodeur/tracking-status-normalizer.git
cd tracking-status-normalizer
pip install -e .[dev]
```

---

# Running Tests

```bash
pytest
```

Current test status:

```text
47 tests passing
0 failures
```

---

# Build Package

Build the package:

```bash
python -m build
```

Expected artifacts:

```text
dist/
├── tracking_status_normalizer-0.5.0.tar.gz
└── tracking_status_normalizer-0.5.0-py3-none-any.whl
```

---

# Continuous Integration

The repository uses GitHub Actions.

The CI workflow validates:

```text
Package installation
Unit tests
Package build
```

The workflow runs on push and pull request events.

---

# Command Line Interface

The package exposes the `tsn` command.

## Process a Shipment File

```bash
tsn process examples/data/dhl_delivery.json
```

Example output:

```text
==================================================
Tracking Status Normalizer
==================================================

Carrier           : DHL
Validation        : VALID
Current Status    : DELIVERED
Outcome           : SUCCESS
Mapped Statuses   : 3
Unmapped Statuses : 0
```

---

# REST API

The project includes a FastAPI application.

## Start the API

```bash
uvicorn tracking_status_normalizer.api.app:app --reload
```

---

## Swagger UI

Swagger documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

## OpenAPI Specification

The OpenAPI contract is available at:

```text
http://127.0.0.1:8000/openapi.json
```

---

# API Endpoints

## GET /health

Health check endpoint.

Example response:

```json
{
  "status": "ok"
}
```

---

## POST /normalize

Normalize a single carrier status.

Request:

```json
{
  "carrier": "DHL",
  "raw_status": "Shipment delivered"
}
```

Response:

```json
{
  "carrier": "DHL",
  "raw_status": "Shipment delivered",
  "canonical_status": "DELIVERED",
  "mapped": true
}
```

---

## POST /validate

Validate a canonical lifecycle.

Request:

```json
{
  "statuses": ["IN_TRANSIT", "OUT_FOR_DELIVERY", "DELIVERED"]
}
```

Response:

```json
{
  "valid": true,
  "reason": null
}
```

Invalid lifecycle example:

```json
{
  "statuses": ["DELIVERED", "IN_TRANSIT"]
}
```

Response:

```json
{
  "valid": false,
  "reason": "Invalid transition: DELIVERED -> IN_TRANSIT"
}
```

---

## POST /process

Process a complete shipment lifecycle from raw carrier statuses.

Request:

```json
{
  "carrier": "DHL",
  "statuses": ["Shipment in transit", "Out for delivery", "Shipment delivered"]
}
```

Response:

```json
{
  "carrier": "DHL",
  "validation": "VALID",
  "validation_reason": null,
  "current_status": "DELIVERED",
  "outcome": "SUCCESS",
  "mapped_statuses": 3,
  "unmapped_statuses": 0
}
```

---

# API Error Format

The API returns structured error responses for business and input errors.

Example:

```json
{
  "error": true,
  "code": "MAPPING_FILE_NOT_FOUND",
  "message": "Mapping file not found: missing-file.json",
  "details": null
}
```

Supported API error codes include:

```text
MAPPING_FILE_NOT_FOUND
INVALID_MAPPING_FILE
UNKNOWN_CANONICAL_STATUS
INVALID_REQUEST
INTERNAL_ERROR
```

---

# Examples

Runnable examples are available in:

```text
examples/
```

Included examples:

```text
normalize_status.py
validate_lifecycle.py
analyze_lifecycle.py
process_shipment.py
coverage_analysis.py
unknown_status_report.py
catalog_analysis.py
load_and_process_shipment.py
```

---

# Example Data

Example shipment files are available in:

```text
examples/data/
```

Included example files:

```text
dhl_delivery.json
colissimo_delivery.json
pickup_expired.json
locker_delivery.json
return_flow.json
invalid_lifecycle.json
```

---

# Mapping Catalog

The default carrier status mapping file is located at:

```text
data/mappings/carrier_status_mapping.json
```

The expected format is:

```json
{
  "mappings": [
    {
      "carrier": "DHL",
      "raw_status": "Shipment delivered",
      "canonical_status": "DELIVERED"
    }
  ]
}
```

---

# Documentation

Project documentation is available in:

```text
docs/
```

Current documentation includes:

```text
status-taxonomy.md
domain-model.md
```

---

# Roadmap

## Completed

```text
Foundation

Canonical Taxonomy

Domain Engine

Normalization Engine

Catalog Governance

Shipment Loader

Command Line Interface

FastAPI REST API

Swagger / OpenAPI

Centralized API Error Handling

GitHub Actions CI

Package Distribution

Release 0.5.0
```

## Next

```text
API Developer Experience

API Error Documentation

Dashboard

PyPI Publication

Release 1.0
```

---

# Technical Highlights

This project demonstrates:

- Python package architecture
- Domain modeling
- State machine design
- Carrier status normalization
- Shipment lifecycle validation
- Catalog governance
- CLI design
- FastAPI API design
- Structured API error handling
- Automated testing
- GitHub Actions CI
- Python packaging

---

# License

MIT License.
