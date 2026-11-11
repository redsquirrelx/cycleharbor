# ADR-0004 — Maintenance queue boundary

**Status:** Accepted

## Context

Maintenance submission will evolve from a local collection to an asynchronous dispatcher.

## Decision

`RepairQueue.enqueue` is the only submission entry point available to `MaintenanceTriage`. Queue internals must not be accessed by business services.

## Consequences

A durable queue can replace the local implementation without edits to triage.
