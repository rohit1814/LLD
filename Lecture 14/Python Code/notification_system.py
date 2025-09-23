## Issue in this code: Client has to know lot about the obervable, then it has to assing them to observers
## then it has to add observers to observable

from abc import ABC, abstractmethod
from typing import List, cast
from datetime import datetime

# ===================================
# Notification Interface & Decorators
# ===================================

class INotification(ABC):
    @abstractmethod
    def get_content(self) -> str:
        pass

class SimpleNotification(INotification):
    def __init__(self, message: str) -> None:
        self.message = message

    def get_content(self) -> str:
        return f"{self.message}"

class INotificationDecorator(INotification):
    def __init__(self, notification: INotification) -> None:
        self._notification = notification


class TimestampDecorator(INotificationDecorator):
    def _get_timestamp(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
class TimestampDecorator(INotificationDecorator):
    def _get_timestamp(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def get_content(self) -> str:
        return f"[Timestamp: {self._get_timestamp()}] {self._notification.get_content()}"

class SignatureDecorator(INotificationDecorator):
    def __init__(self, notification: INotification, signature: str) -> None:
        super().__init__(notification)
        self.signature = signature

    def get_content(self) -> str:
        # include wrapped content and then append signature
        return f"{self._notification.get_content()}\n[Signature: {self.signature}]\n"

# ============================
# Observer Pattern
# ============================


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None:
        pass

class Observable(ABC):
    @abstractmethod
    def add_observer(self, observer: 'IObserver') -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: 'IObserver') -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass

class NotificationObservable(Observable):
    def __init__(self) -> None:
        self._observers: List[IObserver] = []
        self._current_notification: INotification | None = None

    def add_observer(self, observer: 'IObserver') -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: 'IObserver') -> None:
        if observer in self._observers:
            self._observers.remove(observer)
        # self._observers = [obs for obs in self._observers if obs is not observer]

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()

    @property
    def notification(self) -> INotification | None:
        return self._current_notification
    
    @notification.setter
    def notification(self, notification: INotification) -> None:
        self._current_notification = notification
        self.notify_observers()

    def get_notification_content(self) -> str:
        if self._current_notification:
            return self._current_notification.get_content()
        return "No Notification"

class Logger(IObserver):
    def __init__(self, observable: NotificationObservable) -> None:
        self._observable = observable

    def update(self) -> None:
        print("Logging New Notification :")
        print(self._observable.get_notification_content())

# ============================
# Strategy Pattern
# ============================

class INotificationStrategy(ABC):
    @abstractmethod
    def send_notification(self, content: str) -> None:
        pass

class EmailStrategy(INotificationStrategy):
    def __init__(self, email_id: str) -> None:
        self.email_id = email_id

    def send_notification(self, content: str) -> None:
        print(f"Sending Email Notification to {self.email_id} with content:\n{content}")

class SMSStrategy(INotificationStrategy):
    def __init__(self, phone_number: str) -> None:
        self.phone_number = phone_number

    def send_notification(self, content: str) -> None:
        print(f"Sending SMS Notification to {self.phone_number} with content:\n{content}")

class PopupStrategy(INotificationStrategy):

    def send_notification(self, content: str) -> None:
        print(f"Sending Popup Notification:\n{content}")

class NotificationEngine(IObserver):
    def __init__(self, observable: NotificationObservable) -> None:
        self._strategies: List[INotificationStrategy] = []
        self._observable = observable

    def add_notification_strategy(self, strategy: INotificationStrategy) -> None:
        self._strategies.append(strategy)

    def update(self) -> None:
        content = self._observable.get_notification_content()
        for strategy in self._strategies:
            strategy.send_notification(content)

# ============================
# Singleton Notification Service to attach created notifications to push notifications
# ============================

class NotificationService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._observable = NotificationObservable()
            cls._instance._notifications: List[INotification] = []   # This syntax (var: Type = value) inside __new__ can confuse Python because it thinks it’s a local variable annotation, not assigning to an attribute.
            # cls._instance._notifications = cast(List[INotification], [])

        return cls._instance

    def get_observable(self) -> NotificationObservable:
        return self._observable

    def send_notification(self, notification: INotification) -> None:
        self._notifications.append(notification)  # history
        self._observable.notification = notification

# ============================
# Example usage (Client Code)
# ============================

if __name__ == "__main__":
    service = NotificationService()
    observable = service.get_observable()

    logger = Logger(observable)
    engine = NotificationEngine(observable)
    engine.add_notification_strategy(EmailStrategy("test@example.com"))
    engine.add_notification_strategy(SMSStrategy("+911234567890"))
    engine.add_notification_strategy(PopupStrategy())

    observable.add_observer(logger)
    observable.add_observer(engine)

    notif = SimpleNotification("Your order has been shipped!")
    notif = TimestampDecorator(notif)
    notif = SignatureDecorator(notif, "Customer Care")

    service.send_notification(notif)

