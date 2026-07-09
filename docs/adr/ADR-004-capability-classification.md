# ADR-004: Capability Classification Model

## Status

Accepted

## Date

2026-07-09

## Context

The project requires a mechanism to distinguish fundamental engine capabilities from extended logistics coverage.

Initial discussions considered:

- Mandatory
- Recommended
- Optional

These categories were dependent on deployment context.

## Decision

Capabilities will be classified as:

- CORE
- EXTENDED

## CORE

DIRECT_DELIVERY

EXCEPTION_MANAGEMENT

These capabilities form the minimum useful operational coverage of the engine.

## EXTENDED

- PUDO
- LOCKER
- OUT_OF_HOME_DELIVERY
- RETURNS
- CUSTOMS

These capabilities increase operational coverage but are not part of the minimum engine footprint.

## Consequences

Readiness Assessment will rely primarily on CORE capabilities.

EXTENDED capabilities will contribute to recommendations and maturity assessment.
