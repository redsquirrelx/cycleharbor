# CH-105 — Interfaces and contracts

**Status:** Approved · **Baseline:** Python 3.10+ Protocol ports and dataclasses.

## Application ports

| Port | Signature | Guarantee |
|---|---|---|
| `BicycleCatalog` | `find(bike_id)`, `available_at(station_id)` | Returns bicycle domain values; storage representation is hidden |
| `LockGateway` | `unlock(bike_id) -> bool`, `lock(bike_id) -> bool` | Transport acknowledgement normalized to boolean; no dock command dictionaries |
| `RideRepository` | `save(ride)`, `find(ride_id)` | No persistence-specific lookup or write API in business services |
| `FarePolicy` | `quote(ride) -> FareQuote` | Every policy is independently substitutable and returns a complete nonnegative payable quote |
| `PaymentGateway` | `capture(FareQuote) -> PaymentReceipt` | Adapters translate processors' response shapes into a stable domain receipt |
| `MessageGateway` | `send(RiderMessage) -> None` | Delivery contract independent of SMS or email transport |
| `RepairQueue` | `enqueue(RepairTicket) -> None` | Submission contract independent of queue backing store or write strategy |

`PaymentReceipt` is defined in `domain/models.py` with `ride_id`, `external_reference`, `amount_cents`, and `accepted`. The settlement layer checks `accepted` and returns `external_reference`; it cannot inspect processor fields like `paid` or `id`.

`ProcessorPaymentAdapter` and `SandboxPaymentGateway` must both conform to `PaymentGateway` without changes to the settlement service. The payment processor client belongs in the adapter and is not a service constructor dependency.

`FlatFarePolicy`, `MinuteFarePolicy` and `PromotionalFarePolicy` satisfy the same `FarePolicy.quote` contract. Promotions provide the final amount after policy selection, rather than a negative delta that forces downstream callers to distinguish policy families.

The `RepairQueue` abstraction owns how work is queued; the maintenance service may construct the `RepairTicket` but is not permitted to access `MemoryRepairQueue.tickets` or analogous implementation storage.

## Boundary guarantees

`bootstrap.py` is the single location allowed to bind concrete lock, payment, message and queue adapters to service ports. A feature's tests may instantiate fakes conforming to the port without importing deployment adapters. Infrastructure API responses are converted before crossing into the application layer.
