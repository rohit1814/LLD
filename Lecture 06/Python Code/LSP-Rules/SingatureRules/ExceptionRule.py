# A subclass should throw fewer or narrower exceptions (never broader or new unrelated ones) than the parent.

# In C++, this isn’t enforced by the compiler (as your comment says).
# In Python, exceptions are also not enforced by the language, 
# but we can model this with exception hierarchy and type hints to make it clear.

from abc import ABC, abstractmethod


# --- Custom Exception Hierarchy (similar to C++ std::exception family) ---
class LogicError(Exception):
    """Base for logical errors."""


class InvalidArgument(LogicError):
    pass


class DomainError(LogicError):
    pass


class LengthError(LogicError):
    pass


class OutOfRange(LogicError):
    pass


class RuntimeError(Exception):
    """Base for runtime errors."""


class RangeError(RuntimeError):
    pass


class OverflowErrorCustom(RuntimeError):  # To avoid conflict with built-in OverflowError
    pass


class UnderflowError(RuntimeError):
    pass


# --- Parent Class ---
class Parent(ABC):
    def get_value(self) -> None:
        """Parent may raise a LogicError."""
        raise LogicError("Parent error")


# --- Child Class ---
class Child(Parent):
    def get_value(self) -> None:
        """Child may raise OutOfRange (narrower exception)."""
        raise OutOfRange("Child error")
        # ❌ Wrong (would violate LSP):
        # raise RuntimeError("Child Error")


# --- Client Class ---
class Client:
    def __init__(self, p: Parent) -> None:
        self.p = p

    def take_value(self) -> None:
        try:
            self.p.get_value()
        except LogicError as e:  # Catching parent-declared exception
            print(f"Logic error exception occurred: {e}")

if __name__ == "__main__":
    parent = Parent()
    child = Child()

    client = Client(parent)
    # client = Client(child)  # Works fine with Child too

    client.take_value()
