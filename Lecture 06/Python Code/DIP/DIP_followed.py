from abc import ABC, abstractmethod


# Abstraction (Interface)
class Database(ABC):
    @abstractmethod
    def save(self, data: str) -> None:
        pass


# MySQL implementation (Low-level module)
class MySQLDatabase(Database):
    def save(self, data: str) -> None:
        print(f"Executing SQL Query: INSERT INTO users VALUES('{data}');")


# MongoDB implementation (Low-level module)
class MongoDBDatabase(Database):
    def save(self, data: str) -> None:
        print(f"Executing MongoDB Function: db.users.insert({{name: '{data}'}})")


# High-level module (Now loosely coupled)
class UserService:
    def __init__(self, database: Database) -> None:  # Dependency Injection
        self.db = database

    def store_user(self, user: str) -> None:
        self.db.save(user)


if __name__ == "__main__":
    mysql = MySQLDatabase()
    mongodb = MongoDBDatabase()
