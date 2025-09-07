# Note: In python we can use property decorators in place of getters and setters.
# https://www.geeksforgeeks.org/python/observer-method-python-design-patterns/
# Use GPT: to make it more pythonic and simpler, this is a basic implementation of observer pattern in C++/Java

from typing import List


# Observer interface
class ISubscriber:
    def update(self):
        raise NotImplementedError


# Subject (Observable) interface
class IChannel:
    def subscribe(self, subscriber: ISubscriber):
        raise NotImplementedError

    def unsubscribe(self, subscriber: ISubscriber):
        raise NotImplementedError

    def notify_subscribers(self):
        raise NotImplementedError


# Concrete Subject
class Channel(IChannel):
    def __init__(self, name: str):
        self._name = name
        self._subscribers: List[ISubscriber] = []
        self._latest_video: str = ""

    def subscribe(self, subscriber: ISubscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: ISubscriber):
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def notify_subscribers(self):
        for sub in self._subscribers:
            sub.update()

    def upload_video(self, title: str):
        self._latest_video = title
        print(f"\n[{self._name} uploaded \"{title}\"]")
        self.notify_subscribers()

    def get_video_data(self) -> str:
        return f"\nCheckout our new Video : {self._latest_video}\n"


# Concrete Observer
class Subscriber(ISubscriber):
    def __init__(self, name: str, channel: Channel):
        self._name = name
        self._channel = channel

    def update(self):
        print(f"Hey {self._name}, {self._channel.get_video_data()}", end="")


# Example usage
if __name__ == "__main__":
    channel = Channel("CoderArmy")

    subs1 = Subscriber("Varun", channel)
    subs2 = Subscriber("Tarun", channel)

    channel.subscribe(subs1)
    channel.subscribe(subs2)

    channel.upload_video("Observer Pattern Tutorial")

    channel.unsubscribe(subs1)

    channel.upload_video("Decorator Pattern Tutorial")
