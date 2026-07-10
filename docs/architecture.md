# Tracking Status Normalizer - Architecture

## Purpose

Tracking Status Normalizer is a Python application designed to normalize carrier-specific tracking statuses into a standardized canonical status model.

The project provides:

- Status normalization
- Lifecycle validation
- Shipment outcome analysis
- Operational governance
- Reporting and exports

---

## High-Level Architecture

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

## Architectural Principles

### Separation of Concerns

The project is divided into independent layers.

Engine Layer:

- Normalization
- Validation
- Processing
- Lifecycle Analysis

Governance Layer:

- Coverage
- Readiness
- Gap Analysis
- Recommendations
- Maturity
- Reporting

### Single Responsibility

Each module has a clearly defined responsibility.

### Immutable Domain Models

Most domain objects are implemented using frozen dataclasses.

### Testability

Every business component has dedicated unit tests.

### Export Isolation

Exporters never contain business logic.

Exporters only transform existing results into:

- JSON
- Markdown
- CSV
- HTML

---

## Project Layers

### Domain

Core business vocabulary.

Examples:

- CanonicalStatus
- ShipmentOutcome
- StatusCategory

### Normalization

Maps carrier statuses to canonical statuses.

### Validation

Validates lifecycle consistency.

### Analysis

Analyzes shipment lifecycle behavior.

### Processing

Executes full shipment processing workflow.

### Governance

Analyzes catalog maturity and operational readiness.

### Exporters

Transforms Governance Reports into consumable formats.

### CLI

Command line interface.

### API

REST API layer.# Tracking Status Normalizer - Architecture

## Purpose

Tracking Status Normalizer is a Python application designed to normalize carrier-specific tracking statuses into a standardized canonical status model.

The project provides:

- Status normalization
- Lifecycle validation
- Shipment outcome analysis
- Operational governance
- Reporting and exports

---

## High-Level Architecture

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

## Architectural Principles

### Separation of Concerns

The project is divided into independent layers.

Engine Layer:

- Normalization
- Validation
- Processing
- Lifecycle Analysis

Governance Layer:

- Coverage
- Readiness
- Gap Analysis
- Recommendations
- Maturity
- Reporting

### Single Responsibility

Each module has a clearly defined responsibility.

### Immutable Domain Models

Most domain objects are implemented using frozen dataclasses.

### Testability

Every business component has dedicated unit tests.

### Export Isolation

Exporters never contain business logic.

Exporters only transform existing results into:

- JSON
- Markdown
- CSV
- HTML

---

## Project Layers

### Domain

Core business vocabulary.

Examples:

- CanonicalStatus
- ShipmentOutcome
- StatusCategory

### Normalization

Maps carrier statuses to canonical statuses.

### Validation

Validates lifecycle consistency.

### Analysis

Analyzes shipment lifecycle behavior.

### Processing

Executes full shipment processing workflow.

### Governance

Analyzes catalog maturity and operational readiness.

### Exporters

Transforms Governance Reports into consumable formats.

### CLI

Command line interface.

### API

REST API layer.
