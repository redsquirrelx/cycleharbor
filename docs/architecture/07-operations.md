# CH-107 — Operations

**Status:** Approved

Local operation uses `build_local_app()` for a self-contained station fleet and simulated lock control. A deployment profile provides live credentials and adapter settings at composition time. `python -m cycleharbor` performs a single end-to-end rental for operational smoke checks.

Operational tracing should include a ride ID, bicycle ID, selected fare product and payment reference. Payment token material and physical device command payloads are restricted to adapter logs.

Maintenance queue handoff is a separate operational concern from triage rules, allowing the queue to be migrated without changing the triage service.
