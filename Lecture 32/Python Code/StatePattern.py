# Do you also want me to simplify this with Python’s duck typing 
# (i.e., without abstract base class, but just using normal classes)?

from abc import ABC, abstractmethod


# --- Abstract State Interface ---
class VendingState(ABC):
    @abstractmethod
    def insert_coin(self, machine, coin):
        pass

    @abstractmethod
    def select_item(self, machine):
        pass

    @abstractmethod
    def dispense(self, machine):
        pass

    @abstractmethod
    def return_coin(self, machine):
        pass

    @abstractmethod
    def refill(self, machine, quantity):
        pass

    @abstractmethod
    def get_state_name(self):
        pass


# --- Context Class ---
class VendingMachine:
    def __init__(self, item_count: int, item_price: int):
        self.item_count = item_count
        self.item_price = item_price
        self.inserted_coins = 0

        # Create state objects
        self.no_coin_state = NoCoinState()
        self.has_coin_state = HasCoinState()
        self.dispense_state = DispenseState()
        self.sold_out_state = SoldOutState()

        # Set initial state
        self.current_state = (
            self.no_coin_state if item_count > 0 else self.sold_out_state
        )

    # Delegate to current state
    def insert_coin(self, coin: int):
        self.current_state = self.current_state.insert_coin(self, coin)

    def select_item(self):
        self.current_state = self.current_state.select_item(self)

    def dispense(self):
        self.current_state = self.current_state.dispense(self)

    def return_coin(self):
        self.current_state = self.current_state.return_coin(self)

    def refill(self, quantity: int):
        self.current_state = self.current_state.refill(self, quantity)

    def print_status(self):
        print("\n--- Vending Machine Status ---")
        print(f"Items remaining: {self.item_count}")
        print(f"Inserted coin: Rs {self.inserted_coins}")
        print(f"Current state: {self.current_state.get_state_name()}\n")


# --- Concrete States ---
class NoCoinState(VendingState):
    def insert_coin(self, machine, coin):
        machine.inserted_coins = coin
        print(f"Coin inserted. Current balance: Rs {coin}")
        return machine.has_coin_state

    def select_item(self, machine):
        print("Please insert coin first!")
        return machine.no_coin_state

    def dispense(self, machine):
        print("Please insert coin and select item first!")
        return machine.no_coin_state

    def return_coin(self, machine):
        print("No coin to return!")
        return machine.no_coin_state

    def refill(self, machine, quantity):
        print("Items refilling")
        machine.item_count += quantity
        return machine.no_coin_state

    def get_state_name(self):
        return "NO_COIN"


class HasCoinState(VendingState):
    def insert_coin(self, machine, coin):
        machine.inserted_coins += coin
        print(f"Additional coin inserted. Current balance: Rs {machine.inserted_coins}")
        return machine.has_coin_state

    def select_item(self, machine):
        if machine.inserted_coins >= machine.item_price:
            print("Item selected. Dispensing...")
            change = machine.inserted_coins - machine.item_price
            if change > 0:
                print(f"Change returned: Rs {change}")
            machine.inserted_coins = 0
            return machine.dispense_state
        else:
            needed = machine.item_price - machine.inserted_coins
            print(f"Insufficient funds. Need Rs {needed} more.")
            return machine.has_coin_state

    def dispense(self, machine):
        print("Please select an item first!")
        return machine.has_coin_state

    def return_coin(self, machine):
        print(f"Coin returned: Rs {machine.inserted_coins}")
        machine.inserted_coins = 0
        return machine.no_coin_state

    def refill(self, machine, quantity):
        print("Can't refill in this state")
        return machine.has_coin_state

    def get_state_name(self):
        return "HAS_COIN"


class DispenseState(VendingState):
    def insert_coin(self, machine, coin):
        print(f"Please wait, already dispensing item. Coin returned: Rs {coin}")
        return machine.dispense_state

    def select_item(self, machine):
        print("Already dispensing item. Please wait.")
        return machine.dispense_state

    def dispense(self, machine):
        print("Item dispensed!")
        machine.item_count -= 1
        if machine.item_count > 0:
            return machine.no_coin_state
        else:
            print("Machine is now sold out!")
            return machine.sold_out_state

    def return_coin(self, machine):
        print("Cannot return coin while dispensing item!")
        return machine.dispense_state

    def refill(self, machine, quantity):
        print("Can't refill in this state")
        return machine.dispense_state

    def get_state_name(self):
        return "DISPENSING"


class SoldOutState(VendingState):
    def insert_coin(self, machine, coin):
        print(f"Machine is sold out. Coin returned: Rs {coin}")
        return machine.sold_out_state

    def select_item(self, machine):
        print("Machine is sold out!")
        return machine.sold_out_state

    def dispense(self, machine):
        print("Machine is sold out!")
        return machine.sold_out_state

    def return_coin(self, machine):
        print("Machine is sold out. No coin inserted.")
        return machine.sold_out_state

    def refill(self, machine, quantity):
        print("Items refilling")
        machine.item_count += quantity
        return machine.no_coin_state

    def get_state_name(self):
        return "SOLD_OUT"


# --- Usage ---
if __name__ == "__main__":
    print("=== Water Bottle VENDING MACHINE ===")
    machine = VendingMachine(item_count=2, item_price=20)
    machine.print_status()

    print("1. Trying to select item without coin:")
    machine.select_item()
    machine.print_status()

    print("2. Inserting coin:")
    machine.insert_coin(10)
    machine.print_status()

    print("3. Selecting item with insufficient funds:")
    machine.select_item()
    machine.print_status()

    print("4. Adding more coins:")
    machine.insert_coin(10)
    machine.print_status()

    print("5. Selecting item Now")
    machine.select_item()
    machine.print_status()

    print("6. Dispensing item:")
    machine.dispense()
    machine.print_status()

    print("7. Buying last item:")
    machine.insert_coin(20)
    machine.select_item()
    machine.dispense()
    machine.print_status()

    print("8. Trying to use sold out machine:")
    machine.insert_coin(5)

    print("9. Refilling machine:")
    machine.refill(2)
    machine.print_status()
