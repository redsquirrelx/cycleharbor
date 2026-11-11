# CycleHarbor

CycleHarbor manages station-based urban bicycle rentals, including fleet availability, dock locks, active ride sessions, fare calculation, payments, rider notifications, and maintenance reporting. The service exposes an application workflow and a small command-line entrypoint for local operations.

## Development

Python 3.10 or newer; core runtime uses only the Python standard library.

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
python -m cycleharbor
cycleharbor demo
```

Without installation, run `PYTHONPATH=src python -m cycleharbor` (PowerShell: `$env:PYTHONPATH='src'`).

## Project layout

- `src/cycleharbor/domain`: bicycles, riders, rides, fare quotes, receipts and events
- `src/cycleharbor/contracts.py`: infrastructure-independent application ports
- `src/cycleharbor/fleet`, `rides`, `pricing`: fleet and trip management
- `src/cycleharbor/payments`, `notifications`, `maintenance`: operational services
- `src/cycleharbor/integrations`, `storage`: external and local adapters
- `src/cycleharbor/bootstrap.py`: deployment composition

## Architecture

The maintained architecture baseline starts at [docs/architecture.md](docs/architecture.md). The architecture chapters describe ownership, interactions, interfaces, quality properties and verification expectations. Decisions are tracked under `docs/adr/`.
