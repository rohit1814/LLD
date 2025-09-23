from typing import Optional
from models.order import Order  # Make sure your Python Order class exists

class PickupOrder(Order):
    def __init__(self, user=None, restaurant=None, items=None, payment_strategy=None, scheduled: Optional[str] = None):
        if items is None:
            items = []
        super().__init__(user, restaurant, items, payment_strategy, scheduled=scheduled)
        self._restaurant_address: str = ""

    def get_type(self) -> str:
        return "Pickup"

    # --- Property for restaurant_address ---
    @property
    def restaurant_address(self) -> str:
        return self._restaurant_address

    @restaurant_address.setter
    def restaurant_address(self, addr: str) -> None:
        self._restaurant_address = addr
