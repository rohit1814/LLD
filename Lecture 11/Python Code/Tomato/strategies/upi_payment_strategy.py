from strategies.payment_strategy import PaymentStrategy

class UpiPaymentStrategy(PaymentStrategy):
    def __init__(self, upi_id: str):
        self._upi_id = upi_id

    def pay(self, amount: float) -> None:
        print(f"Paid ₹{amount} using UPI ({self._upi_id})")
