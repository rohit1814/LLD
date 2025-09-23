from typing import Optional
from models.order import Order  # Make sure your Python Order class exists

class DeliveryOrder(Order):
    def __init__(self, user=None, restaurant=None, items=None, payment_strategy=None, scheduled: Optional[str] = None):
        if items is None:
            items = []
        super().__init__(user, restaurant, items, payment_strategy, scheduled=scheduled)
        self._user_address: str = ""

    def get_type(self) -> str:
        return "Delivery"

    # --- Property for user_address ---
    @property
    def user_address(self) -> str:
        return self._user_address

    @user_address.setter
    def user_address(self, addr: str) -> None:
        self._user_address = addr
