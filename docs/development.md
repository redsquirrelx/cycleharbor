# Development workflow

**Status:** Maintained

Install editable package with `python -m pip install -e .`; run tests using `python -m unittest discover -s tests -v`. Use `cycleharbor demo` for a local rental walkthrough.

The package is organized around application-owned ports in `contracts.py` and domain dataclasses in `domain/models.py`. New integrations belong in `integrations/` and must be bound in `bootstrap.py`. Feature services may rely on stable port annotations but must remain deployable with non-memory adapters.

Architectural decisions are maintained as ADRs. Update the contracts chapter whenever an API visible to multiple packages changes.
