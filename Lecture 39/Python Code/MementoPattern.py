# Check pythonic code also
# Do you also want me to make this more pythonic using dataclasses 
# for DatabaseMemento and maybe context managers (with transactions)?

class DatabaseMemento:
    """Memento - Stores database state snapshot"""
    def __init__(self, db_data):
        self._data = db_data.copy()  # deep copy to prevent mutation

    def get_state(self):
        return self._data


class Database:
    """Originator - The database whose state we want to save/restore"""
    def __init__(self):
        self.records = {}

    def insert(self, key, value):
        self.records[key] = value
        print(f"Inserted: {key} = {value}")

    def update(self, key, value):
        if key in self.records:
            self.records[key] = value
            print(f"Updated: {key} = {value}")
        else:
            print(f"Key not found for update: {key}")

    def remove(self, key):
        if key in self.records:
            del self.records[key]
            print(f"Deleted: {key}")
        else:
            print(f"Key not found for deletion: {key}")

    def create_memento(self):
        print("Creating database backup...")
        return DatabaseMemento(self.records)

    def restore_from_memento(self, memento: DatabaseMemento):
        self.records = memento.get_state().copy()
        print("Database restored from backup!")

    def display_records(self):
        print("\n--- Current Database State ---")
        if not self.records:
            print("Database is empty")
        else:
            for k, v in self.records.items():
                print(f"{k} = {v}")
        print("-----------------------------\n")


class TransactionManager:
    """Caretaker - Manages the memento (transaction manager)"""
    def __init__(self):
        self.backup = None

    def begin_transaction(self, db: Database):
        print("=== BEGIN TRANSACTION ===")
        self.backup = db.create_memento()

    def commit_transaction(self):
        print("=== COMMIT TRANSACTION ===")
        self.backup = None
        print("Transaction committed successfully!")

    def rollback_transaction(self, db: Database):
        print("=== ROLLBACK TRANSACTION ===")
        if self.backup:
            db.restore_from_memento(self.backup)
            self.backup = None
            print("Transaction rolled back!")
        else:
            print("No backup available for rollback!")


if __name__ == "__main__":
    db = Database()
    tx_manager = TransactionManager()

    # Success scenario
    tx_manager.begin_transaction(db)
    db.insert("user1", "Aditya")
    db.insert("user2", "Rohit")
    tx_manager.commit_transaction()

    db.display_records()

    # Failed scenario
    tx_manager.begin_transaction(db)
    db.insert("user3", "Saurav")
    db.insert("user4", "Manish")

    db.display_records()

    # Some error -> Rollback
    print("ERROR: Something went wrong during transaction!")
    tx_manager.rollback_transaction(db)

    db.display_records()
