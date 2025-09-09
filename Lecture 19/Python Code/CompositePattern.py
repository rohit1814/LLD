from abc import ABC, abstractmethod


# Base interface
class FileSystemItem(ABC):
    @abstractmethod
    def ls(self, indent=0):
        pass

    @abstractmethod
    def open_all(self, indent=0):
        pass

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def cd(self, name: str):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def is_folder(self):
        pass


# Leaf: File
class File(FileSystemItem):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def ls(self, indent=0):
        print(" " * indent + self.name)

    def open_all(self, indent=0):
        print(" " * indent + self.name)

    def get_size(self):
        return self.size

    def cd(self, name: str):
        return None  # Can't cd into a file

    def get_name(self):
        return self.name

    def is_folder(self):
        return False


# Composite: Folder
class Folder(FileSystemItem):
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add(self, item: FileSystemItem):
        self.children.append(item)

    def ls(self, indent=0):
        for child in self.children:
            if child.is_folder():
                print(" " * indent + "+ " + child.get_name())
            else:
                print(" " * indent + child.get_name())

    def open_all(self, indent=0):
        print(" " * indent + "+ " + self.name)
        for child in self.children:
            child.open_all(indent + 4)

    def get_size(self):
        return sum(child.get_size() for child in self.children)

    def cd(self, target: str):
        for child in self.children:
            if child.is_folder() and child.get_name() == target:
                return child
        return None  # not found

    def get_name(self):
        return self.name

    def is_folder(self):
        return True


# Client code
if __name__ == "__main__":
    # Build file system
    root = Folder("root")
    root.add(File("file1.txt", 1))
    root.add(File("file2.txt", 1))

    docs = Folder("docs")
    docs.add(File("resume.pdf", 1))
    docs.add(File("notes.txt", 1))
    root.add(docs)

    images = Folder("images")
    images.add(File("photo.jpg", 1))
    root.add(images)

    # Run commands
    print("\nListing root:")
    root.ls()

    print("\nListing docs:")
    docs.ls()

    print("\nOpen all:")
    root.open_all()

    print("\nChange directory into docs:")
    cwd = root.cd("docs")
    if cwd:
        cwd.ls()
    else:
        print("Could not cd into docs")

    print("\nTotal size:", root.get_size())
