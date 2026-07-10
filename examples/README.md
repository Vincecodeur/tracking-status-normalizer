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

Carrier Statuses
|
v
Normalization Layer
|
v
Canonical Statuses
|
+------------------+
| |
v v
Engine Layer Governance Layer
| |
v v
Processing Coverage / Readiness
Validation Gaps / Recommendations
Analysis Maturity / Reporting
|
v
CLI / API / Exporters

---

# Project Structure

src/tracking_status_normalizer

- domain
- normalization
- validation
- analysis
- processing
- catalog
- governance
- cli
- api
- io

Additional folders:

- docs
- examples
- tests

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
pip install -r requirements.txt
```

---

# Running Tests

Execute the full test suite:

```bash
pytest
```

Expected result for V1.0:

```text
115 passed
0 failed
```

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
