class Car:
    def __init__(self):
        self.speed = 0

    def accelerate(self):
        print("Accelerating")
        self.speed += 20

    # Postcondition: Speed must reduce after brake
    def brake(self):
        print("Applying brakes")
        self.speed -= 20


# ✅ Subclass can strengthen postcondition without breaking LSP
class HybridCar(Car):
    def __init__(self):
        super().__init__()
        self.charge = 0

    # Postcondition: Speed must reduce after brake
    # Postcondition: Charge must increase
    def brake(self):
        print("Applying brakes")
        self.speed -= 20
        self.charge += 10


if __name__ == "__main__":
    hybrid_car: Car = HybridCar()
    hybrid_car.brake()  # Works fine: HybridCar reduces speed and also increases charge
