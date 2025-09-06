from abc import ABC, abstractmethod


# Separate interface for 2D shapes
class TwoDimensionalShape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


# Separate interface for 3D shapes
class ThreeDimensionalShape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def volume(self) -> float:
        pass


# Square implements only the 2D interface
class Square(TwoDimensionalShape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side * self.side


# Rectangle implements only the 2D interface
class Rectangle(TwoDimensionalShape):
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width


# Cube implements the 3D interface
class Cube(ThreeDimensionalShape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return 6 * self.side * self.side

    def volume(self) -> float:
        return self.side * self.side * self.side


if __name__ == "__main__":
    square: TwoDimensionalShape = Square(5)
    rectangle: TwoDimensionalShape = Rectangle(4, 6)
    cube: ThreeDimensionalShape = Cube(3)

    print("Square Area:", square.area())
    print("Rectangle Area:", rectangle.area())
    print("Cube Area:", cube.area())
    print("Cube Volume:", cube.volume())
