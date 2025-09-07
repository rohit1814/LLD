from abc import ABC, abstractmethod

# --- Product 1: Burger ---
class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass

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

# --- Product 2: GarlicBread ---
class GarlicBread(ABC):
    @abstractmethod
    def prepare(self):
        pass

class BasicGarlicBread(GarlicBread):
    def prepare(self):
        print("Preparing Basic Garlic Bread with butter and garlic!")

class CheeseGarlicBread(GarlicBread):
    def prepare(self):
        print("Preparing Cheese Garlic Bread with extra cheese and butter!")

class BasicWheatGarlicBread(GarlicBread):
    def prepare(self):
        print("Preparing Basic Wheat Garlic Bread with butter and garlic!")

class CheeseWheatGarlicBread(GarlicBread):
    def prepare(self):
        print("Preparing Cheese Wheat Garlic Bread with extra cheese and butter!")

# --- Abstract Factory ---
class MealFactory(ABC):
    @abstractmethod
    def create_burger(self, burger_type: str) -> Burger:
        pass

    @abstractmethod
    def create_garlic_bread(self, bread_type: str) -> GarlicBread:
        pass

# --- Concrete Factories ---
class SinghBurger(MealFactory):
    def create_burger(self, burger_type: str) -> Burger:
        if burger_type == "basic":
            return BasicBurger()
        elif burger_type == "standard":
            return StandardBurger()
        elif burger_type == "premium":
            return PremiumBurger()
        else:
            raise ValueError("Invalid burger type!")

    def create_garlic_bread(self, bread_type: str) -> GarlicBread:
        if bread_type == "basic":
            return BasicGarlicBread()
        elif bread_type == "cheese":
            return CheeseGarlicBread()
        else:
            raise ValueError("Invalid garlic bread type!")

class KingBurger(MealFactory):
    def create_burger(self, burger_type: str) -> Burger:
        if burger_type == "basic":
            return BasicWheatBurger()
        elif burger_type == "standard":
            return StandardWheatBurger()
        elif burger_type == "premium":
            return PremiumWheatBurger()
        else:
            raise ValueError("Invalid burger type!")

    def create_garlic_bread(self, bread_type: str) -> GarlicBread:
        if bread_type == "basic":
            return BasicWheatGarlicBread()
        elif bread_type == "cheese":
            return CheeseWheatGarlicBread()
        else:
            raise ValueError("Invalid garlic bread type!")

# --- Client Code ---
if __name__ == "__main__":
    burger_type = "basic"
    garlic_bread_type = "cheese"

    meal_factory = KingBurger()  # could also be SinghBurger()

    burger = meal_factory.create_burger(burger_type)
    garlic_bread = meal_factory.create_garlic_bread(garlic_bread_type)

    burger.prepare()
    garlic_bread.prepare()
