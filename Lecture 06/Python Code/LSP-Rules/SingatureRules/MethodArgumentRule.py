# In Python, the Liskov Substitution Principle (LSP) method argument rule is 
# less strict than C++ because Python is dynamically typed.
from abc import ABC, abstractmethod


# Parent class with method
class Parent(ABC):
    @abstractmethod
    def print(self, msg: str) -> None:
        pass


class Child(Parent):
    # Must keep the same or wider parameter type
    def print(self, msg: str) -> None:
        print(f"Child: {msg}")


# Client expects Parent-like behavior
class Client:
    def __init__(self, p: Parent) -> None:
        self.p = p

    def print_msg(self) -> None:
        # Client passes a string because Parent defines msg: str
        self.p.print("Hello")


if __name__ == "__main__":
    parent = Parent.__subclasses__()[0]  # Just to avoid instantiating abstract Parent
    child = Child()

    # Client can use Child instead of Parent without issues
    client = Client(child)
    client.print_msg()
