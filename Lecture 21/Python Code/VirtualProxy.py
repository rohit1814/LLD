from abc import ABC, abstractmethod

# Subject Interface
class IImage(ABC):
    @abstractmethod
    def display(self):
        pass


# Real Subject
class RealImage(IImage):
    def __init__(self, filename: str):
        self.filename = filename
        # Heavy operation (simulate image loading)
        print(f"[RealImage] Loading image from disk: {self.filename}")

    def display(self):
        print(f"[RealImage] Displaying {self.filename}")


# Proxy
class ImageProxy(IImage):
    def __init__(self, filename: str):
        self.filename = filename
        self._real_image: RealImage | None = None

    def display(self):
        # Lazy initialization
        if self._real_image is None:
            self._real_image = RealImage(self.filename)
        self._real_image.display()


# Client code
if __name__ == "__main__":
    image1: IImage = ImageProxy("sample.jpg")
    image1.display()
