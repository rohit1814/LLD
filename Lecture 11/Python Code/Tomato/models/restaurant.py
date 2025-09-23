# https://www.geeksforgeeks.org/python/python-property-decorator-property/

from typing import List
from models.menu_item import MenuItem  # Assuming you have a MenuItem class in menu_item.py


class Restaurant:
    _next_restaurant_id: int = 0  # class variable

    def __init__(self, name: str, location: str):
        self._name: str = name
        self._location: str = location
        self._menu: List[MenuItem] = []
        Restaurant._next_restaurant_id += 1
        self.restaurant_id: int = Restaurant._next_restaurant_id

    def __del__(self):
        # Optional: debug message when destroyed
        print(f"Destroying Restaurant: {self._name}, and clearing its menu.")
        self._menu.clear()

    # --- Properties for name ---
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, n: str) -> None:
        self._name = n

    # --- Properties for location ---
    @property
    def location(self) -> str:
        return self._location

    @location.setter
    def location(self, loc: str) -> None:
        self._location = loc

    # --- Menu management ---
    def add_menu_item(self, item: MenuItem) -> None:
        self._menu.append(item)

    @property
    def menu(self) -> List[MenuItem]:
        return self._menu
