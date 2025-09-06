# Product class representing any item in eCommerce.
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


# 1. ShoppingCart: Only responsible for cart-related business logic
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


# 3. ShoppingCartStorage: Only responsible for saving cart
class ShoppingCartStorage:
    def __init__(self, cart: ShoppingCart):
        self.cart = cart

    def save_to_sql_database(self):
        print("Saving shopping cart to SQL DB...")

    def save_to_mongo_database(self):
        print("Saving shopping cart to Mongo DB...")

    def save_to_file(self):
        print("Saving shopping cart to File...")


if __name__ == "__main__":
    cart = ShoppingCart()

    cart.add_product(Product("Laptop", 50000))
    cart.add_product(Product("Mouse", 2000))

    printer = ShoppingCartPrinter(cart)
    printer.print_invoice()

    db = ShoppingCartStorage(cart)
    db.save_to_sql_database()
