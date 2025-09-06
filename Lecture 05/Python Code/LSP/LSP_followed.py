from abc import ABC, abstractmethod


class DepositOnlyAccount(ABC):
    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass


class WithdrawableAccount(DepositOnlyAccount):
    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass


class SavingAccount(WithdrawableAccount):
    def __init__(self) -> None:
        self.balance = 0.0

    def deposit(self, amount: float) -> None:
        self.balance += amount
        print(f"Deposited: {amount} in Savings Account. New Balance: {self.balance}")

    def withdraw(self, amount: float) -> None:
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount} from Savings Account. New Balance: {self.balance}")
        else:
            print("Insufficient funds in Savings Account!")


class CurrentAccount(WithdrawableAccount):
    def __init__(self) -> None:
        self.balance = 0.0

    def deposit(self, amount: float) -> None:
        self.balance += amount
        print(f"Deposited: {amount} in Current Account. New Balance: {self.balance}")

    def withdraw(self, amount: float) -> None:
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount} from Current Account. New Balance: {self.balance}")
        else:
            print("Insufficient funds in Current Account!")


class FixedTermAccount(DepositOnlyAccount):
    def __init__(self) -> None:
        self.balance = 0.0

    def deposit(self, amount: float) -> None:
        self.balance += amount
        print(f"Deposited: {amount} in Fixed Term Account. New Balance: {self.balance}")


class BankClient:
    def __init__(self, withdrawable_accounts: list[WithdrawableAccount],
                 deposit_only_accounts: list[DepositOnlyAccount]) -> None:
        self.withdrawable_accounts = withdrawable_accounts
        self.deposit_only_accounts = deposit_only_accounts

    def process_transactions(self) -> None:
        for acc in self.withdrawable_accounts:
            acc.deposit(1000)
            acc.withdraw(500)

        for acc in self.deposit_only_accounts:
            acc.deposit(5000)


if __name__ == "__main__":
    withdrawable_accounts = [SavingAccount(), CurrentAccount()]
    deposit_only_accounts = [FixedTermAccount()]

    client = BankClient(withdrawable_accounts, deposit_only_accounts)
    client.process_transactions()
