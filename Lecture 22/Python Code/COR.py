from abc import ABC, abstractmethod


# Abstract Handler
class MoneyHandler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next_handler(self, next_handler):
        self._next_handler = next_handler

    @abstractmethod
    def dispense(self, amount):
        pass


# Concrete Handler for 1000 Rs Notes
class ThousandHandler(MoneyHandler):
    def __init__(self, num_notes):
        super().__init__()
        self.num_notes = num_notes

    def dispense(self, amount):
        notes_needed = amount // 1000

        if notes_needed > self.num_notes:
            notes_needed = self.num_notes
            self.num_notes = 0
        else:
            self.num_notes -= notes_needed

        if notes_needed > 0:
            print(f"Dispensing {notes_needed} x ₹1000 notes.")

        remaining_amount = amount - (notes_needed * 1000)
        if remaining_amount > 0:
            if self._next_handler:
                self._next_handler.dispense(remaining_amount)
            else:
                print(
                    f"Remaining amount of {remaining_amount} cannot be fulfilled (Insufficient funds in ATM)"
                )


# Concrete Handler for 500 Rs Notes
class FiveHundredHandler(MoneyHandler):
    def __init__(self, num_notes):
        super().__init__()
        self.num_notes = num_notes

    def dispense(self, amount):
        notes_needed = amount // 500

        if notes_needed > self.num_notes:
            notes_needed = self.num_notes
            self.num_notes = 0
        else:
            self.num_notes -= notes_needed

        if notes_needed > 0:
            print(f"Dispensing {notes_needed} x ₹500 notes.")

        remaining_amount = amount - (notes_needed * 500)
        if remaining_amount > 0:
            if self._next_handler:
                self._next_handler.dispense(remaining_amount)
            else:
                print(
                    f"Remaining amount of {remaining_amount} cannot be fulfilled (Insufficient funds in ATM)"
                )


# Concrete Handler for 200 Rs Notes
class TwoHundredHandler(MoneyHandler):
    def __init__(self, num_notes):
        super().__init__()
        self.num_notes = num_notes

    def dispense(self, amount):
        notes_needed = amount // 200

        if notes_needed > self.num_notes:
            notes_needed = self.num_notes
            self.num_notes = 0
        else:
            self.num_notes -= notes_needed

        if notes_needed > 0:
            print(f"Dispensing {notes_needed} x ₹200 notes.")

        remaining_amount = amount - (notes_needed * 200)
        if remaining_amount > 0:
            if self._next_handler:
                self._next_handler.dispense(remaining_amount)
            else:
                print(
                    f"Remaining amount of {remaining_amount} cannot be fulfilled (Insufficient funds in ATM)"
                )


# Concrete Handler for 100 Rs Notes
class HundredHandler(MoneyHandler):
    def __init__(self, num_notes):
        super().__init__()
        self.num_notes = num_notes

    def dispense(self, amount):
        notes_needed = amount // 100

        if notes_needed > self.num_notes:
            notes_needed = self.num_notes
            self.num_notes = 0
        else:
            self.num_notes -= notes_needed

        if notes_needed > 0:
            print(f"Dispensing {notes_needed} x ₹100 notes.")

        remaining_amount = amount - (notes_needed * 100)
        if remaining_amount > 0:
            if self._next_handler:
                self._next_handler.dispense(remaining_amount)
            else:
                print(
                    f"Remaining amount of {remaining_amount} cannot be fulfilled (Insufficient funds in ATM)"
                )


# Client Code
if __name__ == "__main__":
    # Creating handlers for each note type
    thousand_handler = ThousandHandler(3)
    five_hundred_handler = FiveHundredHandler(5)
    two_hundred_handler = TwoHundredHandler(10)
    hundred_handler = HundredHandler(20)

    # Setting up the chain of responsibility
    thousand_handler.set_next_handler(five_hundred_handler)
    five_hundred_handler.set_next_handler(two_hundred_handler)
    two_hundred_handler.set_next_handler(hundred_handler)

    amount_to_withdraw = 4000

    # Initiating the chain
    print(f"\nDispensing amount: ₹{amount_to_withdraw}")
    thousand_handler.dispense(amount_to_withdraw)
