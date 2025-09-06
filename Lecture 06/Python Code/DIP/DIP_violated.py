class MySQLDatabase:  # Low-level module
    def save_to_sql(self, data: str) -> None:
        print(f"Executing SQL Query: INSERT INTO users VALUES('{data}');")


class MongoDBDatabase:  # Low-level module
    def save_to_mongo(self, data: str) -> None:
        print(f"Executing MongoDB Function: db.users.insert({{name: '{data}'}})")


class UserService:  # High-level module (Tightly coupled)
    def __init__(self) -> None:
        self.sql_db = MySQLDatabase()   # Direct dependency on MySQL
        self.mongo_db = MongoDBDatabase()  # Direct dependency on MongoDB

    def store_user_to_sql(self, user: str) -> None:
        # MySQL-specific code
        self.sql_db.save_to_sql(user)

    def store_user_to_mongo(self, user: str) -> None:
        # MongoDB-specific code
        self.mongo_db.save_to_mongo(user)


if __name__ == "__main__":
    service = UserService()
    service.store_user_to_sql("Aditya")
    service.store_user_to_mongo("Rohit")
