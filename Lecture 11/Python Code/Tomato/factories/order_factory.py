from abc import ABC, abstractmethod
from typing import List, Optional
from models.user import User
from models.cart import Cart
from models.restaurant import Restaurant
from models.menu_item import MenuItem
from models.order import Order
from strategies.payment_strategy import PaymentStrategy


class OrderFactory(ABC):
    @abstractmethod
    def create_order(
        self,
        user: Optional[User],
        cart: Optional[Cart],
        restaurant: Optional[Restaurant],
        menu_items: List[MenuItem],
        payment_strategy: Optional[PaymentStrategy],
        total_cost: float,
        order_type: str
    ) -> Order:
        pass
