class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


# Violating SRP: ShoppingCart is handling multiple responsibilities
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def get_products(self):
        return self.products

    # 1. Calculates total price in cart
    def calculate_total(self) -> float:
        return sum(p.price for p in self.products)

    # 2. Violating SRP - Prints invoice (Should be in a separate class)
    def print_invoice(self):
        print("Shopping Cart Invoice:")
        for p in self.products:
            print(f"{p.name} - Rs {p.price}")
        print(f"Total: Rs {self.calculate_total()}")

    # 3. Violating SRP - Saves to DB (Should be in a separate class)
    def save_to_database(self):
        print("Saving shopping cart to database...")


if __name__ == "__main__":
    cart = ShoppingCart()

    cart.add_product(Product("Laptop", 50000))
    cart.add_product(Product("Mouse", 2000))

    cart.print_invoice()
    cart.save_to_database()
