from models.order import Order
from models.menu_item import MenuItem


class NotificationService:
    @staticmethod
    def notify(order: Order) -> None:
        print(f"\nNotification: New {order.get_type()} order placed!")
        print("---------------------------------------------")
        print(f"Order ID: {order.order_id}")
        print(f"Customer: {order.user.get_name()}")
        print(f"Restaurant: {order.restaurant.name}")
        print("Items Ordered:")

        for item in order.items:
            print(f"   - {item.name} (₹{item.price})")

        print(f"Total: ₹{order.total}")
        print(f"Scheduled For: {order.scheduled}")
        print("Payment: Done")
        print("---------------------------------------------")
