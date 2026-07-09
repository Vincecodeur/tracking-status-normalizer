# ADR-001: Engine First Principle

## Status

Accepted

## Date

2026-07-09

## Context

The project started as a Tracking Status Normalizer Engine.

As new governance capabilities were identified, there was a risk of transforming the project into a logistics platform, OMS, WMS, TMS, or Parcel Tracking solution.

## Decision

The project remains primarily a Tracking Status Normalizer Engine.

All future governance capabilities must consume information produced by the engine and must not modify the mission of the engine.

## Consequences

The following remain part of the Engine Layer:

- Normalization
- Validation
- Lifecycle Analysis
- Shipment Processing
- CLI
- REST API

Governance capabilities may be added only if they use engine outputs.

The following are explicitly out of scope:

- User management
- Authentication
- OMS features
- WMS features
- TMS features
- Real-time shipment monitoring
- Notifications
- Contract management

## Principle

Engine First.
Governance Second.
