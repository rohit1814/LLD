from typing import List, Optional
from factories.order_factory import OrderFactory
from models.delivery_order import DeliveryOrder
from models.pickup_order import PickupOrder
from models.user import User
from models.cart import Cart
from models.restaurant import Restaurant
from models.menu_item import MenuItem
from strategies.payment_strategy import PaymentStrategy
from models.order import Order


class ScheduledOrderFactory(OrderFactory):
    def __init__(self, schedule_time: str):
        self._schedule_time = schedule_time

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

        if order_type == "Delivery":
            order = DeliveryOrder(user, restaurant, menu_items, payment_strategy)
            if user and hasattr(user, "address"):
                order.user_address = user.address
        else:
            order = PickupOrder(user, restaurant, menu_items, payment_strategy)
            if restaurant:
                order.restaurant_address = restaurant.location

        # Common attributes
        order.user = user
        order.restaurant = restaurant
        order.items = menu_items
        order.payment_strategy = payment_strategy
        order.scheduled = self._schedule_time
        order.total = total_cost

        return order
