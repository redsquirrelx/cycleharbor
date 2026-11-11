# CH-102 — Functional ownership

**Status:** Approved

| Owner | Responsibility | Dependencies |
|---|---|---|
| `fleet/availability.py` | Read-only inventory availability | `BicycleCatalog` |
| `rides/activation.py` | Eligibility and lock release for new rides | `BicycleCatalog`, `LockGateway`, `RideRepository` |
| `rides/completion.py` | Close rides and confirm locks | `LockGateway`, `RideRepository` |
| `pricing/policies.py` | Produce complete domain `FareQuote` values | `FarePolicy` contract |
| `payments/settlement.py` | Capture an issued fare and process `PaymentReceipt` | `PaymentGateway`, `RideRepository`, `FarePolicy` |
| `notifications/service.py` | Prepare rider-facing message content | `MessageGateway` |
| `maintenance/triage.py` | Evaluate field reports and issue repair tickets | `RepairQueue` |
| `reporting/usage.py` | Compute read-only durations | `RideRepository` |
| `integrations/` | Map infrastructure protocols to domain contracts | External clients |
| `bootstrap.py` | Choose adapters and wire constructors | All concrete implementation choices |

Business services receive ports through constructor injection. They must not instantiate or import implementation classes from `integrations/` or `storage/`; this ownership ensures that a storage, payment or queue replacement cannot require a business service change.

The maintenance triage service owns ticket preparation and sends records through `RepairQueue.enqueue`. It must not append directly to a local queue's internal list; the queue may be synchronous locally and asynchronous in field deployments.
