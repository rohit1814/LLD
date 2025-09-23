from typing import List, Optional
from models.restaurant import Restaurant
from models.menu_item import MenuItem


class Cart:
    def __init__(self):
        self._restaurant: Optional[Restaurant] = None
        self._items: List[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        if not self._restaurant:
            print("Cart: Set a restaurant before adding items.")
            return
        self._items.append(item)

    def get_total_cost(self) -> float:
        return sum(item.price for item in self._items)

    def is_empty(self) -> bool:
        return self._restaurant is None or len(self._items) == 0

    def clear(self) -> None:
        self._items.clear()
        self._restaurant = None

    # --- Getters and setters ---
    @property
    def restaurant(self) -> Optional[Restaurant]:
        return self._restaurant

    @restaurant.setter
    def restaurant(self, r: Restaurant) -> None:
        self._restaurant = r

    @property
    def items(self) -> List[MenuItem]:
        return self._items
