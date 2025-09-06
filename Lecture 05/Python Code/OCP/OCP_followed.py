from abc import ABC, abstractmethod


# Product class representing any item in eCommerce
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


# 1. ShoppingCart: Only responsible for Cart-related business logic
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def get_products(self):
        return self.products

    # Calculates total price in cart
    def calculate_total(self) -> float:
        return sum(p.price for p in self.products)


# 2. ShoppingCartPrinter: Only responsible for printing invoices
class ShoppingCartPrinter:
    def __init__(self, cart: ShoppingCart):
        self.cart = cart

    def print_invoice(self):
        print("Shopping Cart Invoice:")
        for p in self.cart.get_products():
            print(f"{p.name} - Rs {p.price}")
        print(f"Total: Rs {self.cart.calculate_total()}")


# Abstract class for persistence
class Persistence(ABC):
    @abstractmethod
    def save(self, cart: ShoppingCart):
        pass


class SQLPersistence(Persistence):
    def save(self, cart: ShoppingCart):
        print("Saving shopping cart to SQL DB...")


class MongoPersistence(Persistence):
    def save(self, cart: ShoppingCart):
        print("Saving shopping cart to MongoDB...")


class FilePersistence(Persistence):
    def save(self, cart: ShoppingCart):
        print("Saving shopping cart to a file...")


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_product(Product("Laptop", 50000))
    cart.add_product(Product("Mouse", 2000))

    printer = ShoppingCartPrinter(cart)
    printer.print_invoice()

    db = SQLPersistence()
    mongo = MongoPersistence()
    file = FilePersistence()

    db.save(cart)     # Save to SQL database
    mongo.save(cart)  # Save to MongoDB
    file.save(cart)   # Save to File
