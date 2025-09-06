class DocumentEditor:
    def __init__(self):
        self.document_elements = []
        self.rendered_document = ""

    # Adds text as a plain string
    def add_text(self, text: str):
        self.document_elements.append(text)

    # Adds an image represented by its file path
    def add_image(self, image_path: str):
        self.document_elements.append(image_path)

    # Renders the document by checking the type of each element at runtime
    def render_document(self) -> str:
        if not self.rendered_document:
            result = ""
            for element in self.document_elements:
                if element.lower().endswith((".jpg", ".png")):
                    result += f"[Image: {element}]\n"
                else:
                    result += element + "\n"
            self.rendered_document = result
        return self.rendered_document

    # Saves the rendered document to a file
    def save_to_file(self, filename="document.txt"):
        try:
            with open(filename, "w") as file:
                file.write(self.render_document())
            print(f"Document saved to {filename}")
        except IOError:
            print("Error: Unable to open file for writing.")


if __name__ == "__main__":
    editor = DocumentEditor()
    editor.add_text("Hello, world!")
    editor.add_image("picture.jpg")
    editor.add_text("This is a document editor.")

    print(editor.render_document())
    editor.save_to_file()
