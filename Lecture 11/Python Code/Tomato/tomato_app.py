from typing import List, Optional
from models.user import User
from models.restaurant import Restaurant
from models.menu_item import MenuItem
from models.cart import Cart
from managers.restaurant_manager import RestaurantManager
from managers.order_manager import OrderManager
from strategies.payment_strategy import PaymentStrategy
from strategies.upi_payment_strategy import UpiPaymentStrategy
from factories.new_order_factory import NewOrderFactory
from factories.scheduled_order_factory import ScheduledOrderFactory
from services.notification_service import NotificationService
from utils.time_utils import TimeUtils
from models.order import Order


class TomatoApp:
    def __init__(self):
        self.initialize_restaurants()

    def initialize_restaurants(self):
        restaurant1 = Restaurant("Bikaner", "Delhi")
        restaurant1.add_menu_item(MenuItem("P1", "Chole Bhature", 120))
        restaurant1.add_menu_item(MenuItem("P2", "Samosa", 15))

        restaurant2 = Restaurant("Haldiram", "Kolkata")
        restaurant2.add_menu_item(MenuItem("P1", "Raj Kachori", 80))
        restaurant2.add_menu_item(MenuItem("P2", "Pav Bhaji", 100))
        restaurant2.add_menu_item(MenuItem("P3", "Dhokla", 50))

        restaurant3 = Restaurant("Saravana Bhavan", "Chennai")
        restaurant3.add_menu_item(MenuItem("P1", "Masala Dosa", 90))
        restaurant3.add_menu_item(MenuItem("P2", "Idli Vada", 60))
        restaurant3.add_menu_item(MenuItem("P3", "Filter Coffee", 30))

        restaurant_manager = RestaurantManager()
        restaurant_manager.add_restaurant(restaurant1)
        restaurant_manager.add_restaurant(restaurant2)
        restaurant_manager.add_restaurant(restaurant3)

        # Add other sample restaurants if needed

    def search_restaurants(self, location: str) -> List[Restaurant]:
        return RestaurantManager().search_by_location(location)

    def select_restaurant(self, user: User, restaurant: Restaurant) -> None:
        cart = user.cart
        cart.restaurant = restaurant

    def add_to_cart(self, user: User, item_code: str) -> None:
        restaurant = user.cart.restaurant
        if not restaurant:
            print("Please select a restaurant first.")
            return
        for item in restaurant.menu:
            if item.code == item_code:
                user.cart.add_item(item)
                break

    def checkout_now(self, user: User, order_type: str, payment_strategy: PaymentStrategy) -> Optional[Order]:
        return self.checkout(user, order_type, payment_strategy, NewOrderFactory())

    def checkout_scheduled(
        self, user: User, order_type: str, payment_strategy: PaymentStrategy, schedule_time: str
    ) -> Optional[Order]:
        return self.checkout(user, order_type, payment_strategy, ScheduledOrderFactory(schedule_time))

    def checkout(
        self,
        user: User,
        order_type: str,
        payment_strategy: PaymentStrategy,
        order_factory
    ) -> Optional[Order]:
        if user.cart.is_empty():
            return None

        user_cart = user.cart
        ordered_restaurant = user_cart.restaurant
        items_ordered = user_cart.items
        total_cost = user_cart.get_total_cost()

        order = order_factory.create_order(
            user, user_cart, ordered_restaurant, items_ordered, payment_strategy, total_cost, order_type
        )
        OrderManager().add_order(order)
        return order

    def pay_for_order(self, user: User, order: Order) -> None:
        is_payment_success = order.process_payment()
        if is_payment_success:
            NotificationService.notify(order)
            user.cart.clear()

    def print_user_cart(self, user: User) -> None:
        print("Items in cart:")
        print("------------------------------------")
        for item in user.cart.items:
            print(f"{item.code} : {item.name} : ₹{item.price}")
        print("------------------------------------")
        print(f"Grand total : ₹{user.cart.get_total_cost()}")
