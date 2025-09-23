from typing import List
from models.order import Order  # Assuming you have a Python Order class in models/order.py


class OrderManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderManager, cls).__new__(cls)
            cls._instance._orders: List[Order] = []
        return cls._instance

    def add_order(self, order: Order) -> None:
        self._orders.append(order)

    def list_orders(self) -> None:
        print("\n--- All Orders ---")
        for order in self._orders:
            print(
                f"{order.get_type()} order for {order.get_user().get_name()} "
                f"| Total: ₹{order.get_total()} "
                f"| At: {order.get_scheduled()}"
            )
