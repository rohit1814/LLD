from abc import ABC, abstractmethod
from typing import List


# Observer interface
class Subscriber(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        ...


# Subject (Observable)
class Channel:
    def __init__(self, name: str):
        self.name = name
        self._subscribers: List[Subscriber] = []

    def subscribe(self, subscriber: Subscriber) -> None:
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber) -> None:
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def notify_subscribers(self, message: str) -> None:
        for sub in self._subscribers:
            sub.update(message)

    def upload_video(self, title: str) -> None:
        print(f"\n[{self.name} uploaded \"{title}\"]")
        self.notify_subscribers(f"Checkout our new Video: {title}")


# Concrete Observer
class User(Subscriber):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str) -> None:
        print(f"Hey {self.name}, {message}")

    def __str__(self):
        return self.name


# Example usage
if __name__ == "__main__":
    channel = Channel("CoderArmy")

    varun = User("Varun")
    tarun = User("Tarun")

    channel.subscribe(varun)
    channel.subscribe(tarun)

    channel.upload_video("Observer Pattern Tutorial")

    channel.unsubscribe(varun)

    channel.upload_video("Decorator Pattern Tutorial")
