from abc import ABC, abstractmethod

# Implementation Hierarchy: Engine interface (LLL)
class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

# Concrete Implementors (LLL)
class PetrolEngine(Engine):
    def start(self):
        print("Petrol engine starting with ignition!")

class DieselEngine(Engine):
    def start(self):
        print("Diesel engine roaring to life!")

class ElectricEngine(Engine):
    def start(self):
        print("Electric engine powering up silently!")

# Abstraction Hierarchy: Car (HLL)
class Car(ABC):
    def __init__(self, engine: Engine):
        self.engine = engine

    @abstractmethod
    def drive(self):
        pass

# Refined Abstraction: Sedan
class Sedan(Car):
    def drive(self):
        self.engine.start()
        print("Driving a Sedan on the highway.")

# Refined Abstraction: SUV
class SUV(Car):
    def drive(self):
        self.engine.start()
        print("Driving an SUV off-road.")


# Client code
if __name__ == "__main__":
    # Create Engine implementations
    petrol_eng = PetrolEngine()
    diesel_eng = DieselEngine()
    electric_eng = ElectricEngine()

    # Create Car abstractions, injecting Engine implementations
    my_sedan = Sedan(petrol_eng)
    my_suv = SUV(electric_eng)
    your_suv = SUV(diesel_eng)

    # Use the cars
    my_sedan.drive()   # Petrol engine + Sedan
    my_suv.drive()     # Electric engine + SUV
    your_suv.drive()   # Diesel engine + SUV
