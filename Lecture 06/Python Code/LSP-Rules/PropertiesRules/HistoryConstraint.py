class BankAccount:
    def __init__(self, balance: float):
        if balance < 0:
            raise ValueError("Balance can't be negative")
        self._balance = balance

    # History Constraint: Withdraw should always be allowed
    def withdraw(self, amount: float):
        if self._balance - amount < 0:
            raise RuntimeError("Insufficient funds")
        self._balance -= amount
        print(f"Amount withdrawn. Remaining balance is {self._balance}")


class FixedDepositAccount(BankAccount):
    def __init__(self, balance: float):
        super().__init__(balance)

    # ❌ LSP Violation: Parent allowed withdraw, child disallows it
    def withdraw(self, amount: float):
        raise RuntimeError("Withdraw not allowed in Fixed Deposit")


if __name__ == "__main__":
    account = BankAccount(100)
    account.withdraw(100)

    # Uncomment to see LSP violation
    # fd_account = FixedDepositAccount(100)
    # fd_account.withdraw(50)   # Breaks client expectation!
