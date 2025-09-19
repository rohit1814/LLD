# Key Differences from C++:
# Python doesn’t need explicit destructors (delete) — garbage collector handles cleanup.
# Instead of dynamic_cast, Python naturally preserves the type when cloning.
# copy.deepcopy() simulates the behavior of a C++ copy constructor.

# Do you also want me to show a more Pythonic variant (without explicit setters, 
# using dataclass and direct attribute assignment)?

import copy


# Prototype interface
class Cloneable:
    def clone(self):
        raise NotImplementedError("Clone method must be implemented")


class NPC(Cloneable):
    def __init__(self, name, health, attack, defense):
        # imagine: call database, complex setup
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        print(f"Setting up template NPC '{self.name}'")

    # the clone method required by Prototype
    def clone(self):
        cloned_obj = copy.deepcopy(self)  # deep copy to simulate C++ copy constructor
        print(f"Cloning NPC '{self.name}'")
        return cloned_obj

    def describe(self):
        print(f"NPC {self.name} [HP={self.health} ATK={self.attack} DEF={self.defense}]")

    # setters
    def set_name(self, name):
        self.name = name

    def set_health(self, health):
        self.health = health

    def set_attack(self, attack):
        self.attack = attack

    def set_defense(self, defense):
        self.defense = defense


if __name__ == "__main__":
    # 1) build one “heavy” template
    alien = NPC("Alien", 30, 5, 2)

    # 2) quickly clone + tweak as many variants as you like
    alien_copied1 = alien.clone()
    alien_copied1.describe()

    alien_copied2 = alien.clone()
    alien_copied2.set_name("Powerful Alien")
    alien_copied2.set_health(50)
    alien_copied2.describe()
