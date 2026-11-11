"""Deployment composition: infrastructure adapters are assembled here."""
from cycleharbor.domain.models import Bicycle
from cycleharbor.storage.memory import MemoryBicycleCatalog, MemoryRideRepository, MemoryRepairQueue
from cycleharbor.integrations.locks import SimulatedLockGateway
from cycleharbor.integrations.payments import ProcessorClient, ProcessorPaymentAdapter
from cycleharbor.pricing.policies import FlatFarePolicy
from cycleharbor.rides.activation import RideActivationService
from cycleharbor.rides.completion import RideCompletionService
from cycleharbor.payments.settlement import SettlementService
from cycleharbor.notifications.gateways import MemoryMessageGateway
from cycleharbor.notifications.service import RiderNotificationService
from cycleharbor.application.workflow import RideWorkflow
from cycleharbor.maintenance.triage import MaintenanceTriage

def build_local_app():
    bikes = MemoryBicycleCatalog([Bicycle("bk-100", "station-west")])
    rides = MemoryRideRepository()
    locks = SimulatedLockGateway()
    payments = ProcessorPaymentAdapter(ProcessorClient("development"))
    notifications = MemoryMessageGateway()
    workflow = RideWorkflow(
        RideActivationService(bikes, locks, rides),
        RideCompletionService(rides, locks),
        SettlementService(rides, FlatFarePolicy(), payments),
        RiderNotificationService(notifications),
    )
    return workflow, MaintenanceTriage(MemoryRepairQueue())
