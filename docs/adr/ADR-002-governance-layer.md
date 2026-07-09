# ADR-002: Governance Layer Architecture

## Status

Accepted

## Date

2026-07-09

## Context

The project needs governance capabilities such as reporting, gap analysis and maturity assessment.

The challenge is to avoid introducing dependencies from the engine to governance features.

## Decision

A dedicated Governance Layer will be introduced.

The Engine Layer remains fully independent.

## Architecture

Engine Layer

- domain
- normalization
- validation
- analysis
- processing
- io

Governance Layer

- coverage
- readiness
- gaps
- recommendations
- maturity
- reporting

## Dependency Rule

Allowed:

Engine -> Governance

Forbidden:

Governance -> Engine modifications

## Consequences

Removing the Governance Layer must not impact the behavior of the Tracking Status Normalizer Engine.
