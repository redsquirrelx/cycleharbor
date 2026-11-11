# ADR-0002 — Payment processor independence

**Status:** Accepted

## Context

Processors return vendor-specific transaction fields and status codes. Settlement logic must operate consistently across production and sandbox gateways.

## Decision

`PaymentGateway.capture` returns `PaymentReceipt`, a domain value with `accepted` and `external_reference`. Both `ProcessorPaymentAdapter` and `SandboxPaymentGateway` implement the same port. Only `bootstrap.py` selects and constructs concrete gateways.

## Consequences

Payment provider migrations change adapters and deployment configuration, not the settlement service.
