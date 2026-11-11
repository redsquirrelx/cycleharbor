"""Domain entities shared by fleet and trip services."""
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Bicycle:
    bike_id: str
    station_id: str
    operational: bool = True

@dataclass(frozen=True)
class Rider:
    rider_id: str
    active: bool = True

@dataclass(frozen=True)
class Ride:
    ride_id: str
    rider_id: str
    bike_id: str
    started_at: datetime
    ended_at: datetime | None = None

@dataclass(frozen=True)
class FareQuote:
    ride_id: str
    amount_cents: int
    currency: str = "USD"

@dataclass(frozen=True)
class PaymentReceipt:
    ride_id: str
    external_reference: str
    amount_cents: int
    accepted: bool

@dataclass(frozen=True)
class RiderMessage:
    rider_id: str
    template: str
    body: str

@dataclass(frozen=True)
class RepairTicket:
    bike_id: str
    problem: str
    opened_at: datetime
