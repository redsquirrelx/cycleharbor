"""External payment adapters and local sandbox gateway."""
from cycleharbor.domain.models import FareQuote, PaymentReceipt

class SandboxPaymentGateway:
    def __init__(self):
        self.captures: list[FareQuote] = []
    def capture(self, quote: FareQuote) -> PaymentReceipt:
        self.captures.append(quote)
        return PaymentReceipt(quote.ride_id, f"sbx-{len(self.captures)}", quote.amount_cents, True)

class ProcessorClient:
    def __init__(self, merchant_key: str):
        self.merchant_key = merchant_key
    def post_capture(self, payload: dict) -> dict:
        return {"id": "processor-001", "paid": True, "amount": payload["amount"]}

class ProcessorPaymentAdapter:
    """Maps domain fare quotes to processor requests."""
    def __init__(self, client: ProcessorClient):
        self.client = client
    def capture(self, quote: FareQuote) -> dict:
        # The processor response remains available to downstream settlement callers.
        return self.client.post_capture({"amount": quote.amount_cents, "currency": quote.currency, "reference": quote.ride_id})
