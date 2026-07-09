# Tracking Status Normalizer

A Python domain engine for carrier status normalization, shipment lifecycle validation, and tracking analytics.

## Overview

Tracking carriers use different status vocabularies:

| Carrier         | Raw Status            |
| --------------- | --------------------- |
| DHL             | Shipment delivered    |
| UPS             | Delivered             |
| Amazon Shipping | Package delivered     |
| Colissimo       | Votre colis est livré |

The Tracking Status Normalizer converts those carrier-specific statuses into a shared canonical language:

```text
DELIVERED
```

This enables:

- Multi-carrier tracking
- OMS integration
- WMS integration
- TMS integration
- Parcel Tracking platforms
- Analytics and reporting
- Shipment lifecycle validation

---

# Features

## Canonical Status Taxonomy

The project provides a carrier-agnostic shipment tracking model.

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

### Categories

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

## Status Normalization

Convert carrier-specific statuses into canonical statuses.

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

## Shipment Lifecycle Validation

Validate shipment status progression using a state machine.

Valid:

```text
IN_TRANSIT
↓
OUT_FOR_DELIVERY
↓
DELIVERED
```

Invalid:

```text
DELIVERED
↓
IN_TRANSIT
```

---

## Lifecycle Analysis

Analyze a shipment lifecycle and calculate:

- Current Status
- Status Category
- Shipment Outcome
- Terminal State
- Return Flow Presence
- Exception Presence

---

## Shipment Processor

End-to-end shipment processing.

Flow:

```text
Raw Statuses
    ↓
Normalization
    ↓
Validation
    ↓
Analysis
    ↓
Shipment Result
```

---

## Coverage Analysis

Measure catalog coverage.

Example:

```text
Total Statuses:      100
Mapped Statuses:      92
Unmapped Statuses:     8

Coverage:           92%
```

---

## Catalog Governance

Includes:

- Catalog Analyzer
- Unknown Status Detector
- Unmapped Report Generator

The engine helps identify missing mappings and improve catalog quality over time.

---

# Supported Logistics Flows

The taxonomy supports:

✅ Home Delivery

✅ Business Delivery

✅ Pickup Point (PUDO)

✅ Locker Delivery

✅ Customer Collection

✅ Delivery Failures

✅ Expired Pickup Windows

✅ Automatic Returns

✅ Customer Returns

✅ Customs Processing

✅ Shipment Loss

✅ Damaged Shipments

✅ Exception Management

---

# Project Architecture

```text
src/
└── tracking_status_normalizer/
    │
    ├── domain/
    ├── validation/
    ├── analysis/
    ├── normalization/
    ├── catalog/
    ├── processing/
    └── io/
```

## Domain

Core business model:

- Canonical Statuses
- Categories
- Outcomes
- Transitions

## Validation

Business rule engine:

- Status validation
- Lifecycle validation

## Analysis

Shipment lifecycle analysis.

## Normalization

Carrier status normalization.

## Catalog

Catalog quality and governance.

## Processing

End-to-end shipment processing.

## IO

Input file loading.

---

# Examples

The repository includes runnable examples.

## Normalize Status

```bash
python examples/normalize_status.py
```

## Validate Lifecycle

```bash
python examples/validate_lifecycle.py
```

## Analyze Lifecycle

```bash
python examples/analyze_lifecycle.py
```

## Process Shipment

```bash
python examples/process_shipment.py
```

## Coverage Analysis

```bash
python examples/coverage_analysis.py
```

## Unknown Status Report

```bash
python examples/unknown_status_report.py
```

## Catalog Analysis

```bash
python examples/catalog_analysis.py
```

---

# Example Data

Example shipment files can be found in:

```text
examples/data/
```

Examples include:

```text
dhl_delivery.json
colissimo_delivery.json
pickup_expired.json
locker_delivery.json
return_flow.json
invalid_lifecycle.json
```

---

# Running Tests

Execute all tests:

```bash
pytest
```

Current Result:

```text
37 passed
```

---

# Roadmap

## Completed

```text
✅ Epic 1 - Foundation

✅ Epic 2 - Canonical Taxonomy

✅ Epic 3 - Domain Engine

✅ Epic 4 - Normalization Engine

✅ Epic 5 - Catalog Governance

✅ Epic 5.5 - Shipment File Loading
```

## In Progress

```text
🚧 Epic 6 - Command Line Interface (CLI)
```

## Planned

```text
📅 Epic 7 - REST API

📅 Epic 8 - Dashboard

📅 Epic 9 - Release v1.0
```

---

# Learning Objectives

This project demonstrates:

- Python Architecture
- Domain-Driven Design (DDD)
- State Machine Modeling
- Logistics and Tracking Concepts
- Data Quality Management
- Catalog Governance
- Test-Driven Development
- Multi-Carrier Integration Patterns

---

# License

This project is licensed under the MIT License.

## Continuous Integration

GitHub Actions validates:

- Unit tests
- Package installation
- Wheel build

for every push and pull request.
