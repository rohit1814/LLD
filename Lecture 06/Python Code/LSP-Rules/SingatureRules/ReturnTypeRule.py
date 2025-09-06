# In C++:
# A derived class can override a method and return the same type or a subtype (narrower type).
# That’s called return type covariance, and the compiler enforces it.

# In Python:
# Python is dynamically typed, so it doesn’t enforce return type rules at runtime.
# But if we use type hints + static checkers like mypy, we can model the same rule.

from abc import ABC, abstractmethod


class Animal:
    # Some common Animal methods
    def speak(self) -> str:
        return "Some generic animal sound"


class Dog(Animal):
    # Additional Dog methods specific to Dogs
    def speak(self) -> str:
        return "Woof!"


class Parent(ABC):
    @abstractmethod
    def get_animal(self) -> Animal:
        """Return an Animal (or subclass)."""
        pass


class Child(Parent):
    # Allowed: returning Dog (subclass of Animal)
    def get_animal(self) -> Dog:
        print("Child: Returning Dog instance")
        return Dog()


class Client:
    def __init__(self, p: Parent) -> None:
        self.p = p

    def take_animal(self) -> None:
        animal = self.p.get_animal()
        print(f"Client got an animal that says: {animal.speak()}")
