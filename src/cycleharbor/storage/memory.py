"""Local adapters used by the development profile."""
from cycleharbor.domain.models import Bicycle, Ride, RepairTicket

class MemoryBicycleCatalog:
    def __init__(self, bikes: list[Bicycle] | None = None):
        self._bikes = {bike.bike_id: bike for bike in (bikes or [])}
    def find(self, bike_id: str) -> Bicycle | None:
        return self._bikes.get(bike_id)
    def available_at(self, station_id: str) -> list[Bicycle]:
        return [bike for bike in self._bikes.values() if bike.station_id == station_id and bike.operational]

class MemoryRideRepository:
    def __init__(self):
        self._rides: dict[str, Ride] = {}
    def save(self, ride: Ride) -> None:
        self._rides[ride.ride_id] = ride
    def find(self, ride_id: str) -> Ride | None:
        return self._rides.get(ride_id)

class MemoryRepairQueue:
    def __init__(self):
        self.tickets: list[RepairTicket] = []
    def enqueue(self, ticket: RepairTicket) -> None:
        self.tickets.append(ticket)
