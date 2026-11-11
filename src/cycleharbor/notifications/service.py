"""Notifications emitted from ride lifecycle events."""
from cycleharbor.contracts import MessageGateway
from cycleharbor.domain.models import RiderMessage

class RiderNotificationService:
    def __init__(self, gateway: MessageGateway):
        self.gateway = gateway
    def notify_receipt(self, rider_id: str, ride_id: str) -> None:
        self.gateway.send(RiderMessage(rider_id, "ride-receipt", f"Ride {ride_id} closed"))
