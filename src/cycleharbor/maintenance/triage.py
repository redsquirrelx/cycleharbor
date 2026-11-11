"""Triage of field reports and repair scheduling."""
from datetime import datetime
from cycleharbor.storage.memory import MemoryRepairQueue
from cycleharbor.domain.models import RepairTicket

class MaintenanceTriage:
    def __init__(self, repairs: MemoryRepairQueue):
        self.repairs = repairs
    def report(self, bike_id: str, problem: str, when: datetime) -> RepairTicket:
        ticket = RepairTicket(bike_id, problem, when)
        self.repairs.tickets.append(ticket)
        return ticket
