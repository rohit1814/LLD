# Mediator Design Pattern Example in Python
# You can do more pythonic implementation of this pattern

from typing import List, Tuple


# ─────────────── Mediator Interface ───────────────
class IMediator:
    def register_colleague(self, colleague: "Colleague") -> None:
        raise NotImplementedError

    def send(self, sender: str, msg: str) -> None:
        raise NotImplementedError

    def send_private(self, sender: str, receiver: str, msg: str) -> None:
        raise NotImplementedError


# ─────────────── Colleague Interface ───────────────
class Colleague:
    def __init__(self, mediator: IMediator):
        self.mediator = mediator
        self.mediator.register_colleague(self)

    def get_name(self) -> str:
        raise NotImplementedError

    def send(self, msg: str) -> None:
        raise NotImplementedError

    def send_private(self, to: str, msg: str) -> None:
        raise NotImplementedError

    def receive(self, sender: str, msg: str) -> None:
        raise NotImplementedError


# ─────────────── Concrete Mediator ───────────────
class ChatMediator(IMediator):
    def __init__(self):
        self.colleagues: List[Colleague] = []
        self.mutes: List[Tuple[str, str]] = []  # (muter, muted)

    def register_colleague(self, colleague: Colleague) -> None:
        self.colleagues.append(colleague)

    def mute(self, who: str, whom: str) -> None:
        self.mutes.append((who, whom))

    def send(self, sender: str, msg: str) -> None:
        print(f"[{sender} broadcasts]: {msg}")
        for colleague in self.colleagues:
            if colleague.get_name() == sender:
                continue

            is_muted = any(sender == muted and colleague.get_name() == muter
                           for muter, muted in self.mutes)

            if not is_muted:
                colleague.receive(sender, msg)

    def send_private(self, sender: str, receiver: str, msg: str) -> None:
        print(f"[{sender} → {receiver}]: {msg}")
        for colleague in self.colleagues:
            if colleague.get_name() == receiver:
                for muter, muted in self.mutes:
                    if sender == muted and receiver == muter:
                        print("\n[Message is muted]")
                        return
                colleague.receive(sender, msg)
                return
        print(f"[Mediator] User \"{receiver}\" not found")


# ─────────────── Concrete Colleague ───────────────
class User(Colleague):
    def __init__(self, name: str, mediator: IMediator):
        self.name = name
        super().__init__(mediator)

    def get_name(self) -> str:
        return self.name

    def send(self, msg: str) -> None:
        self.mediator.send(self.name, msg)

    def send_private(self, to: str, msg: str) -> None:
        self.mediator.send_private(self.name, to, msg)

    def receive(self, sender: str, msg: str) -> None:
        print(f"    {self.name} got from {sender}: {msg}")


# ─────────────── Demo ───────────────
if __name__ == "__main__":
    chat_room = ChatMediator()

    user1 = User("Rohan", chat_room)
    user2 = User("Neha", chat_room)
    user3 = User("Mohan", chat_room)

    # Rohan mutes Mohan
    chat_room.mute("Rohan", "Mohan")

    # broadcast from Rohan
    user1.send("Hello Everyone!")

    # private from Mohan to Neha
    user3.send_private("Neha", "Hey Neha!")
