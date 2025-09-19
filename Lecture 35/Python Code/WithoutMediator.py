# Each User knows *all* the others directly.
# If you have N users, you wind up wiring N*(N–1)/2 connections,
# and every new feature (mute, private send, logging...) lives in User too.

class User:
    def __init__(self, name: str):
        self.name = name
        self.peers = []          # List of connected users
        self.muted_users = []    # Users this user has muted

    # manually connect every pair → N^2 wiring
    def add_peer(self, user: "User"):
        self.peers.append(user)

    def mute(self, user_to_mute: str):
        self.muted_users.append(user_to_mute)

    def is_muted(self, user_name: str) -> bool:
        return user_name in self.muted_users

    # broadcast to all peers
    def send(self, msg: str):
        print(f"[{self.name} broadcasts]: {msg}")
        for peer in self.peers:
            if not peer.is_muted(self.name):
                peer.receive(self.name, msg)

    # private send
    def send_to(self, target: "User", msg: str):
        print(f"[{self.name} → {target.name}]: {msg}")
        if not target.is_muted(self.name):
            target.receive(self.name, msg)

    def receive(self, sender: str, msg: str):
        print(f"    {self.name} got from {sender}: {msg}")


# Example usage
if __name__ == "__main__":
    # create users
    user1 = User("Rohan")
    user2 = User("Neha")
    user3 = User("Mohan")

    # wire up peers (each knows each other)
    user1.add_peer(user2)
    user2.add_peer(user1)

    user1.add_peer(user3)
    user3.add_peer(user1)

    user2.add_peer(user3)
    user3.add_peer(user2)

    # mute example: Rohan mutes Mohan
    user1.mute("Mohan")

    # broadcast
    user1.send("Hello everyone!")

    # private
    user3.send_to(user2, "Hey Neha!")
