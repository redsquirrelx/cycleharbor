"""Fleet availability queries."""
from cycleharbor.contracts import BicycleCatalog

class AvailabilityService:
    def __init__(self, catalog: BicycleCatalog):
        self.catalog = catalog
    def list_available(self, station_id: str) -> list[str]:
        return [bike.bike_id for bike in self.catalog.available_at(station_id)]
