from typing import List
from models.restaurant import Restaurant

class RestaurantManager:
    _instance = None  # class-level singleton instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(RestaurantManager, cls).__new__(cls)
            cls._instance._restaurants: List[Restaurant] = []
        return cls._instance

    @property
    def restaurants(self) -> List[Restaurant]:
        return self._restaurants

    def add_restaurant(self, restaurant: Restaurant) -> None:
        self._restaurants.append(restaurant)

    def search_by_location(self, loc: str) -> List[Restaurant]:
        loc = loc.lower()
        return [r for r in self._restaurants if r.location.lower() == loc]
