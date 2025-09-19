# Check more pythonic code for this pattern
# Do you also want me to make it more Pythonic by removing the explicit visit_* boilerplate (using dynamic dispatch)?

from abc import ABC, abstractmethod

# Visitor Interface
class FileSystemVisitor(ABC):
    @abstractmethod
    def visit_text(self, file): pass
    
    @abstractmethod
    def visit_image(self, file): pass
    
    @abstractmethod
    def visit_video(self, file): pass


# Base Component
class FileSystemItem(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def accept(self, visitor: FileSystemVisitor):
        pass


# Concrete Elements
class TextFile(FileSystemItem):
    def __init__(self, name: str, content: str):
        super().__init__(name)
        self.content = content

    def get_content(self):
        return self.content

    def accept(self, visitor: FileSystemVisitor):
        visitor.visit_text(self)


class ImageFile(FileSystemItem):
    def __init__(self, name: str):
        super().__init__(name)

    def accept(self, visitor: FileSystemVisitor):
        visitor.visit_image(self)


class VideoFile(FileSystemItem):
    def __init__(self, name: str):
        super().__init__(name)

    def accept(self, visitor: FileSystemVisitor):
        visitor.visit_video(self)


# Concrete Visitors
class SizeCalculationVisitor(FileSystemVisitor):
    def visit_text(self, file: TextFile):
        print(f"Calculating size for TEXT file: {file.name}")

    def visit_image(self, file: ImageFile):
        print(f"Calculating size for IMAGE file: {file.name}")

    def visit_video(self, file: VideoFile):
        print(f"Calculating size for VIDEO file: {file.name}")


class CompressionVisitor(FileSystemVisitor):
    def visit_text(self, file: TextFile):
        print(f"Compressing TEXT file: {file.name}")

    def visit_image(self, file: ImageFile):
        print(f"Compressing IMAGE file: {file.name}")

    def visit_video(self, file: VideoFile):
        print(f"Compressing VIDEO file: {file.name}")


class VirusScanningVisitor(FileSystemVisitor):
    def visit_text(self, file: TextFile):
        print(f"Scanning TEXT file: {file.name}")

    def visit_image(self, file: ImageFile):
        print(f"Scanning IMAGE file: {file.name}")

    def visit_video(self, file: VideoFile):
        print(f"Scanning VIDEO file: {file.name}")


# Client code
if __name__ == "__main__":
    img1 = ImageFile("sample.jpg")
    img1.accept(SizeCalculationVisitor())
    img1.accept(CompressionVisitor())
    img1.accept(VirusScanningVisitor())

    vid1 = VideoFile("test.mp4")
    vid1.accept(CompressionVisitor())
