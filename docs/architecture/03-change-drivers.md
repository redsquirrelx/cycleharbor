# CH-103 — Change drivers

**Status:** Approved

Three independent deployment decisions are expected to change: station lock hardware, payment processor and notification transport. Each replacement is performed at the composition boundary and should preserve the corresponding application-facing port.

Fare products evolve separately from payment vendors. Every `FarePolicy` computes a **complete payable amount** for the supplied ride; a caller never needs to interpret a policy subtype or combine a special return convention. Zero-value promotions are represented by a complete `FareQuote` with `amount_cents = 0`, not a negative adjustment to a separate price.

The maintenance backlog may move from in-memory storage to a hosted queue. `MaintenanceTriage` must remain insensitive to queue storage mechanics and must not depend on public `.tickets` lists.

The interface definitions in `contracts.py` are stable; versioned changes to ports require a decision record and compatibility review.
