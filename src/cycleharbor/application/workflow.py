"""Application entrypoint for a complete rental session."""
from datetime import datetime, timedelta
from cycleharbor.rides.activation import RideActivationService
from cycleharbor.rides.completion import RideCompletionService
from cycleharbor.payments.settlement import SettlementService
from cycleharbor.notifications.service import RiderNotificationService

class RideWorkflow:
    def __init__(self, activation: RideActivationService, completion: RideCompletionService,
                 settlement: SettlementService, notifications: RiderNotificationService):
        self.activation, self.completion = activation, completion
        self.settlement, self.notifications = settlement, notifications
    def run(self, ride_id: str, rider_id: str, bike_id: str, when: datetime) -> str:
        self.activation.start(ride_id, rider_id, bike_id, when)
        self.completion.finish(ride_id, when + timedelta(minutes=12))
        receipt_id = self.settlement.settle(ride_id)
        self.notifications.notify_receipt(rider_id, ride_id)
        return receipt_id
