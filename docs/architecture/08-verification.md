# CH-108 — Verification

**Status:** Approved

The test suite covers inventory filtering, ride activation and completion, rate calculations, notifications and the local workflow. Interface verification is also part of the architecture review process:

- Both payment adapters produce `PaymentReceipt` values consumed identically by `SettlementService`.
- Payment services rely only on `PaymentGateway` and can be supplied with a fake without requiring processor SDK behavior.
- A promotional fare can replace the standard fare policy and still produce a complete nonnegative quote.
- Repair submission uses `RepairQueue.enqueue` and is compatible with a queue that has no public in-memory list.
- Both simulated and controller-backed lock adapters satisfy the same boolean `LockGateway` contract.

These checks establish substitution semantics rather than only construction or method-name compatibility.
