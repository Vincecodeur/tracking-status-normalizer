# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by Keep a Changelog and Semantic Versioning.

---

## [0.5.0] - 2026-07-09

### Added

#### Command Line Interface

- Added `tsn` command line interface.
- Added `tsn process` command.
- Added shipment JSON file processing through the CLI.
- Added formatted CLI output for shipment processing results.

#### REST API

- Added FastAPI application layer.
- Added `GET /health` endpoint.
- Added `POST /normalize` endpoint.
- Added `POST /validate` endpoint.
- Added `POST /process` endpoint.
- Added Swagger UI documentation through FastAPI.
- Added OpenAPI specification generation.

#### API Error Handling

- Added centralized API error handling.
- Added structured API error responses.
- Added stable API error codes:
  - `MAPPING_FILE_NOT_FOUND`
  - `INVALID_MAPPING_FILE`
  - `UNKNOWN_CANONICAL_STATUS`
  - `INVALID_REQUEST`
  - `INTERNAL_ERROR`

#### Packaging

- Updated project version to `0.5.0`.
- Added Python package build validation.
- Added wheel and source distribution generation.
- Added development dependency for package building.

#### Continuous Integration

- Added GitHub Actions CI workflow.
- Added automated test execution on push and pull request.
- Added automated package build validation in CI.

### Changed

- Updated API version from `0.4.0` to `0.5.0`.
- Updated package version from `0.4.0` to `0.5.0`.
- Improved API contract consistency.
- Replaced default FastAPI `detail` error responses for business errors with structured error payloads.

### Tests

- Expanded automated test suite to cover:
  - CLI behavior
  - FastAPI endpoints
  - API error handling
  - Normalize endpoint
  - Validate endpoint
  - Process endpoint

Current test status:

````text
47 tests passing
0 failures


## [0.4.0] - 2026-07-08

### Added

#### Canonical Tracking Taxonomy

- Added 23 canonical shipment statuses
- Added 8 status categories
- Added shipment outcomes
- Added terminal and quasi-terminal status definitions
- Added support for:
  - Home delivery
  - Business delivery
  - Pickup points (PUDO)
  - Locker delivery
  - Customer returns
  - Automatic returns
  - Customs processing
  - Shipment exceptions

#### Domain Model

- Added StatusCategory model
- Added ShipmentOutcome model
- Added CanonicalStatus model
- Added StatusDefinition model
- Added StateTransition model
- Added MappingRule model
- Added CarrierStatus model
- Added TrackingEvent model definitions

#### Validation Engine

- Added transition registry
- Added transition validator
- Added lifecycle validator
- Added ValidationResult model

#### Analysis Engine

- Added LifecycleSummary model
- Added lifecycle analyzer
- Added support for:
  - Current status analysis
  - Outcome analysis
  - Exception detection
  - Return flow detection

#### Normalization Engine

- Added status normalizer
- Added carrier status model
- Added mapping rule model
- Added JSON mapping catalog
- Added mapping loader
- Added text normalization engine
- Added normalization result object

#### Catalog Governance

- Added unknown status detector
- Added coverage analyzer
- Added catalog analyzer
- Added unmapped status report generator
- Added coverage metrics

#### Shipment Processing

- Added ShipmentResult
- Added Shipment Processor
- Added end-to-end shipment workflow:
  - Normalize
  - Validate
  - Analyze
  - Summarize

#### Input / Output

- Added ShipmentFile model
- Added shipment loader
- Added JSON shipment ingestion

#### Examples

Added runnable examples:

- normalize_status.py
- validate_lifecycle.py
- analyze_lifecycle.py
- process_shipment.py
- coverage_analysis.py
- unknown_status_report.py
- catalog_analysis.py

#### Example Data

Added example shipment files:

- dhl_delivery.json
- colissimo_delivery.json
- pickup_expired.json
- locker_delivery.json
- return_flow.json
- invalid_lifecycle.json

### Tests

Added automated tests for:

- status registry
- lifecycle validation
- lifecycle analysis
- mapping loader
- normalizer
- shipment loader
- shipment processor
- text normalization
- transition validator
- coverage analyzer
- unknown status detection
- unmapped report generation

Current test status:

```text
37 tests passing
0 failures
````

### Architecture

Added packages:

```text
domain/
validation/
analysis/
normalization/
catalog/
processing/
io/
```

---

## [0.3.0] - 2026-07-08

### Added

- Lifecycle validation engine
- Lifecycle analysis engine
- Status registry
- Transition registry
- Transition validator
- Shipment outcomes
- Terminal status support

---

## [0.2.0] - 2026-07-08

### Added

- Canonical shipment taxonomy
- Status categories
- Domain model
- Documentation:
  - status-taxonomy.md
  - domain-model.md

---

## [0.1.0] - 2026-07-08

### Added

- Initial project structure
- Python package setup
- GitHub repository
- Test framework
- pyproject.toml
- README
- LICENSE
- CHANGELOG
- Examples structure
- Documentation structure

---

## Upcoming

### [0.5.0] - Planned

#### CLI

Planned additions:

```bash
tsn process shipment.json

tsn validate shipment.json

tsn coverage

tsn unknown-statuses
```

---

### [0.6.0] - Planned

#### REST API

Planned additions:

- FastAPI integration
- OpenAPI documentation
- JSON endpoints

---

### [0.7.0] - Planned

#### Dashboard

Planned additions:

- Coverage dashboard
- Catalog analytics
- Unknown status monitoring

---

### [1.0.0] - Planned

#### First Stable Release

Goals:

- Stable API
- CLI
- Dashboard
- Documentation
- Full test suite
- Public release
