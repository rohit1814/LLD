class NPC:
    def __init__(self, name: str, health: int, attack: int, defense: int):
        # Imagine heavy operations: DB calls, complex calculations...
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

        print(f"Creating NPC '{name}' [HP:{health}, ATK:{attack}, DEF:{defense}]")

    def describe(self):
        print(f"  NPC: {self.name} | HP={self.health} ATK={self.attack} DEF={self.defense}")


if __name__ == "__main__":
    # Base Alien
    alien = NPC("Alien", 30, 5, 2)
    alien.describe()

    # Powerful Alien — must re-pass all stats, easy to make mistakes
    alien2 = NPC("Powerful Alien", 30, 5, 5)
    alien2.describe()

    # If you want 100 aliens, you'd repeat this many times…
