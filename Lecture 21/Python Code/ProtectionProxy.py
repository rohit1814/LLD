from abc import ABC, abstractmethod

# Interface for Document Reader
class IDocumentReader(ABC):
    @abstractmethod
    def unlock_pdf(self, file_path: str, password: str):
        pass


# Concrete Class: Reads the PDF (simulated)
class RealDocumentReader(IDocumentReader):
    def unlock_pdf(self, file_path: str, password: str):
        print(f"[RealDocumentReader] Unlocking PDF at: {file_path}")
        print(f"[RealDocumentReader] PDF unlocked successfully with password: {password}")
        print("[RealDocumentReader] Displaying PDF content...")


# User class with membership status
class User:
    def __init__(self, name: str, is_premium: bool):
        self.name = name
        self.premium_membership = is_premium


# Proxy Class: Controls access to RealDocumentReader
class DocumentProxy(IDocumentReader):
    def __init__(self, user: User):
        self.real_reader = RealDocumentReader()
        self.user = user

    def unlock_pdf(self, file_path: str, password: str):
        if not self.user.premium_membership:
            print("[DocumentProxy] Access denied. Only premium members can unlock PDFs.")
            return

        # Forwarding the request to the real reader
        self.real_reader.unlock_pdf(file_path, password)


# Client code
if __name__ == "__main__":
    user1 = User("Rohan", False)   # Non Premium User
    user2 = User("Rashmi", True)   # Premium User

    print("== Rohan (Non-Premium) tries to unlock PDF ==")
    doc_reader = DocumentProxy(user1)
    doc_reader.unlock_pdf("protected_document.pdf", "secret123")

    print("\n== Rashmi (Premium) unlocks PDF ==")
    doc_reader = DocumentProxy(user2)
    doc_reader.unlock_pdf("protected_document.pdf", "secret123")
