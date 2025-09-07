# https://www.geeksforgeeks.org/python/factory-method-python-design-patterns/

from abc import ABC, abstractmethod

# --- Product Interface ---
class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass

# --- Concrete Products ---
class BasicBurger(Burger):
    def prepare(self):
        print("Preparing Basic Burger with bun, patty, and ketchup!")

class StandardBurger(Burger):
    def prepare(self):
        print("Preparing Standard Burger with bun, patty, cheese, and lettuce!")

class PremiumBurger(Burger):
    def prepare(self):
        print("Preparing Premium Burger with gourmet bun, premium patty, cheese, lettuce, and secret sauce!")

# --- Factory ---
class BurgerFactory:
    @staticmethod
    def create_burger(burger_type: str) -> Burger:
        if burger_type == "basic":
            return BasicBurger()
        elif burger_type == "standard":
            return StandardBurger()
        elif burger_type == "premium":
            return PremiumBurger()
        else:
            raise ValueError("Invalid burger type!")

# --- Client Code ---
if __name__ == "__main__":
    burger_type = "standard"   # could be "basic" / "premium"
    burger = BurgerFactory.create_burger(burger_type)
    burger.prepare()
