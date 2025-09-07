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

class BasicWheatBurger(Burger):
    def prepare(self):
        print("Preparing Basic Wheat Burger with bun, patty, and ketchup!")

class StandardWheatBurger(Burger):
    def prepare(self):
        print("Preparing Standard Wheat Burger with bun, patty, cheese, and lettuce!")

class PremiumWheatBurger(Burger):
    def prepare(self):
        print("Preparing Premium Wheat Burger with gourmet bun, premium patty, cheese, lettuce, and secret sauce!")

# --- Abstract Factory ---
class BurgerFactory(ABC):
    @abstractmethod
    def create_burger(self, burger_type: str) -> Burger:
        pass

# --- Concrete Factories ---
class SinghBurger(BurgerFactory):
    def create_burger(self, burger_type: str) -> Burger:
        if burger_type == "basic":
            return BasicBurger()
        elif burger_type == "standard":
            return StandardBurger()
        elif burger_type == "premium":
            return PremiumBurger()
        else:
            raise ValueError("Invalid burger type!")

class KingBurger(BurgerFactory):
    def create_burger(self, burger_type: str) -> Burger:
        if burger_type == "basic":
            return BasicWheatBurger()
        elif burger_type == "standard":
            return StandardWheatBurger()
        elif burger_type == "premium":
            return PremiumWheatBurger()
        else:
            raise ValueError("Invalid burger type!")

# --- Client Code ---
if __name__ == "__main__":
    burger_type = "basic"

    # Choose factory
    my_factory = SinghBurger()   # could also be KingBurger()

    burger = my_factory.create_burger(burger_type)
    burger.prepare()
