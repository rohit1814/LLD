class BankAccount:
    def __init__(self, balance: float):
        if balance < 0:
            raise ValueError("Balance can't be negative")
        self._balance = balance   # protected by convention

    def withdraw(self, amount: float):
        if self._balance - amount < 0:
            raise RuntimeError("Insufficient funds")
        self._balance -= amount
        print(f"Amount withdrawn. Remaining balance is {self._balance}")


# ❌ Breaks invariant: allows negative balances
class CheatAccount(BankAccount):
    def __init__(self, balance: float):
        super().__init__(balance)

    def withdraw(self, amount: float):
        # Breaks invariant: allows negative balance
        self._balance -= amount
        print(f"Amount withdrawn. Remaining balance is {self._balance}")


if __name__ == "__main__":
    account = BankAccount(100)
    account.withdraw(100)

    # Uncomment to see LSP violation
    # cheat = CheatAccount(100)
    # cheat.withdraw(200)   # Balance becomes -100 → invariant broken!
