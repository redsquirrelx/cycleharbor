"""Local and external rider communication adapters."""
from cycleharbor.domain.models import RiderMessage

class MemoryMessageGateway:
    def __init__(self):
        self.sent: list[RiderMessage] = []
    def send(self, message: RiderMessage) -> None:
        self.sent.append(message)

class SmsTransport:
    def post_sms(self, destination: str, text: str) -> dict:
        return {"message_id": f"sms-{destination}", "status": "queued"}

class SmsMessageAdapter:
    def __init__(self, transport: SmsTransport):
        self.transport = transport
    def send(self, message: RiderMessage) -> None:
        self.transport.post_sms(message.rider_id, message.body)
