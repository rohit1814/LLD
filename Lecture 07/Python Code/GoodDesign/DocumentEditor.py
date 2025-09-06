from abc import ABC, abstractmethod


# Abstraction for document elements
class DocumentElement(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


# Concrete implementation for text elements
class TextElement(DocumentElement):
    def __init__(self, text: str):
        self.text = text

    def render(self) -> str:
        return self.text


# Concrete implementation for image elements
class ImageElement(DocumentElement):
    def __init__(self, image_path: str):
        self.image_path = image_path

    def render(self) -> str:
        return f"[Image: {self.image_path}]"


# NewLineElement represents a line break in the document
class NewLineElement(DocumentElement):
    def render(self) -> str:
        return "\n"


# TabSpaceElement represents a tab space in the document
class TabSpaceElement(DocumentElement):
    def render(self) -> str:
        return "\t"


# Document class responsible for holding a collection of elements
class Document:
    def __init__(self):
        self.document_elements: list[DocumentElement] = []

    def add_element(self, element: DocumentElement):
        self.document_elements.append(element)

    def render(self) -> str:
        return "".join(element.render() for element in self.document_elements)


# Persistence abstraction
class Persistence(ABC):
    @abstractmethod
    def save(self, data: str):
        pass


# FileStorage implementation of Persistence
class FileStorage(Persistence):
    def __init__(self, filename: str = "document.txt"):
        self.filename = filename

    def save(self, data: str):
        try:
            with open(self.filename, "w") as f:
                f.write(data)
            print(f"Document saved to {self.filename}")
        except IOError:
            print("Error: Unable to open file for writing.")


# Placeholder DBStorage implementation
class DBStorage(Persistence):
    def save(self, data: str):
        # Placeholder for DB saving logic
        print("Document saved to database (placeholder)")


# DocumentEditor class managing client interactions
class DocumentEditor:
    def __init__(self, document: Document, storage: Persistence):
        self.document = document
        self.storage = storage
        self.rendered_document = ""

    def add_text(self, text: str):
        self.document.add_element(TextElement(text))

    def add_image(self, image_path: str):
        self.document.add_element(ImageElement(image_path))

    def add_new_line(self):
        self.document.add_element(NewLineElement())

    def add_tab_space(self):
        self.document.add_element(TabSpaceElement())

    def render_document(self) -> str:
        if not self.rendered_document:
            self.rendered_document = self.document.render()
        return self.rendered_document

    def save_document(self):
        self.storage.save(self.render_document())


# Client usage example
if __name__ == "__main__":
    document = Document()
    persistence = FileStorage()
    editor = DocumentEditor(document, persistence)

    editor.add_text("Hello, world!")
    editor.add_new_line()
    editor.add_text("This is a real-world document editor example.")
    editor.add_new_line()
    editor.add_tab_space()
    editor.add_text("Indented text after a tab space.")
    editor.add_new_line()
    editor.add_image("picture.jpg")

    print(editor.render_document())
    editor.save_document()
