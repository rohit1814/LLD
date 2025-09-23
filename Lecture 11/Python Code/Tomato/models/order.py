from abc import ABC, abstractmethod
from typing import List, Optional
from models.user import User
from models.restaurant import Restaurant
from models.menu_item import MenuItem
from strategies.payment_strategy import PaymentStrategy


class Order(ABC):
    _next_order_id: int = 0  # class variable
    
    def __init__(
        self, 
        user: User, 
        restaurant: Restaurant, 
        items: List[MenuItem], 
        payment_strategy: PaymentStrategy, 
        scheduled: Optional[str] = None
    ):
        Order._next_order_id += 1
        self._order_id: int = Order._next_order_id
        self._user: User = user
        self._restaurant: Restaurant = restaurant
        self._items: List[MenuItem] = items
        self._payment_strategy: PaymentStrategy = payment_strategy
        self._scheduled: Optional[str] = scheduled
        self._total: float = sum(item.price for item in items)

    def __del__(self):
        # In Python, garbage collection handles most cleanup,
        # but if PaymentStrategy holds resources, you could free them here.
        self._payment_strategy = None  # cleanup

    def process_payment(self) -> bool:
        if self._payment_strategy:
            self._payment_strategy.pay(self._total)
            return True
        else:
            print("Please choose a payment mode first")
            return False

    # --- Abstract method ---
    @abstractmethod
    def get_type(self) -> str:
        pass

    # --- Properties ---
    @property
    def order_id(self) -> int:
        return self._order_id

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, user: User) -> None:
        self._user = user

    @property
    def restaurant(self) -> Restaurant:
        return self._restaurant

    @restaurant.setter
    def restaurant(self, restaurant: Restaurant) -> None:
        self._restaurant = restaurant

    @property
    def items(self) -> List[MenuItem]:
        return self._items

    @items.setter
    def items(self, items: List[MenuItem]) -> None:
        self._items = items
        self._total = sum(item.price for item in items)

    @property
    def payment_strategy(self) -> PaymentStrategy:
        return self._payment_strategy

    @payment_strategy.setter
    def payment_strategy(self, payment_strategy: PaymentStrategy) -> None:
        self._payment_strategy = payment_strategy

    @property
    def scheduled(self) -> Optional[str]:
        return self._scheduled

    @scheduled.setter
    def scheduled(self, scheduled: str) -> None:
        self._scheduled = scheduled

    @property
    def total(self) -> float:
        return self._total

    @total.setter
    def total(self, total: float) -> None:
        self._total = total
