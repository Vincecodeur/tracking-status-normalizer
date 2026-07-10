# Tracking Status Normalizer

A production-oriented Python project that standardizes carrier-specific tracking events into a unified canonical tracking model.

The project provides:

- Carrier status normalization
- Shipment lifecycle validation
- Shipment outcome analysis
- Carrier catalog coverage analysis
- Governance assessment and reporting
- CLI and API interfaces
- Multiple report export formats

---

# Features

## Normalization Engine

Convert carrier-specific tracking statuses into standardized canonical statuses.

Examples:

| Carrier Status   | Canonical Status |
| ---------------- | ---------------- |
| In transit       | IN_TRANSIT       |
| Out for delivery | OUT_FOR_DELIVERY |
| Delivered        | DELIVERED        |

---

## Lifecycle Validation

Detect invalid shipment histories.

Examples:

- Delivered before In Transit
- Delivered before Out For Delivery
- Invalid lifecycle transitions

---

## Shipment Analysis

Analyze shipment lifecycle behavior and determine:

- Current canonical status
- Shipment outcome
- Validation status
- Unmapped statuses

---

## Governance Layer

Analyze carrier catalog completeness and operational readiness.

Capabilities:

- Operational Coverage
- Readiness Assessment
- Gap Analysis
- Recommendations
- Maturity Assessment
- Governance Reporting

---

## Report Exporters

Supported formats:

- JSON
- Markdown
- CSV
- HTML

---

# Architecture

## High-Level Overview

```text
Carrier Statuses
        │
        ▼
Normalization Layer
        │
        ▼
Canonical Statuses
        │
        ├──────────────► Engine Layer
        │                   │
        │                   ├─ Validation
        │                   ├─ Analysis
        │                   └─ Processing
        │
        ▼
Governance Layer
        │
        ├─ Coverage
        ├─ Readiness
        ├─ Gaps
        ├─ Recommendations
        ├─ Maturity
        └─ Reporting
                │
                ▼
            Exporters
                │
                ▼
            CLI / API
```

---

# Project Structure

```text
src/tracking_status_normalizer

├── domain
├── normalization
├── validation
├── analysis
├── processing
├── catalog
├── governance
├── cli
├── api
└── io
```

Additional folders:

```text
docs/
examples/
tests/
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>

cd tracking-status-normalizer
```

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -e .
```

Development environment:

```bash
pip install -e ".[dev]"
```

API support:

```bash
pip install -e ".[api]"
```

---

# Running Tests

Execute the full test suite:

```bash
pytest
```

The project is expected to maintain a fully passing test suite.

---

# Command Line Usage

## Process Shipment

```bash
tsn process shipment.json
```

Using a custom mapping file:

```bash
tsn process shipment.json --mapping custom_mapping.json
```

---

## Governance Report

Markdown:

```bash
tsn governance
```

or

```bash
tsn governance --format markdown
```

JSON:

```bash
tsn governance --format json
```

CSV:

```bash
tsn governance --format csv
```

HTML:

```bash
tsn governance --format html
```

---

# Governance Model

The Governance Layer evaluates carrier catalog quality.

Pipeline:

```text
Coverage
    ↓
Readiness
    ↓
Gap Analysis
    ↓
Recommendations
    ↓
Maturity
    ↓
Governance Report
```

## Coverage Levels

- FULL
- PARTIAL
- NONE

## Readiness Levels

- GO
- GO_WITH_RISKS
- NO_GO

## Gap Severity

- CRITICAL
- MEDIUM
- LOW

## Recommendation Priority

- HIGH
- MEDIUM
- LOW

## Maturity Levels

- BASIC
- DEVELOPING
- MATURE
- ADVANCED

---

# Examples

Example files are available under:

```text
examples/
```

Included resources:

### Sample Inputs

- sample_shipment.json
- sample_mapping.json

### Business Scenarios

- colissimo_delivery.json
- dhl_delivery.json
- invalid_lifecycle.json
- locker_delivery.json
- pickup_expired.json
- return_flow.json

### Example Reports

- governance_report.json
- governance_report.md
- governance_report.csv

### Example Scripts

- normalize_status.py
- process_shipment.py
- validate_lifecycle.py
- analyze_lifecycle.py
- coverage_analysis.py
- catalog_analysis.py
- unknown_status_report.py

---

# Documentation

Additional documentation is available in:

```text
docs/
```

Key documents:

- architecture.md
- governance-architecture.md
- cli-guide.md
- exporters-guide.md
- carrier-governance-model.md
- domain-model.md
- status-taxonomy.md

---

# Quality

Current quality objectives:

- Layered architecture
- Separation of concerns
- ADR-driven design
- Export isolation
- Comprehensive unit testing
- CLI integration
- API integration

---

# Project Status

Current Status:

```text
Stable Release
```

Implemented:

- Core Engine
- Governance Layer
- Reporting
- Exporters
- CLI
- API
- Examples
- Documentation

Current version:

```text
v1.0.0
```

---

# License

MIT License
