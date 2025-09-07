import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()  # Lock for thread safety

    def __init__(self):
        print("Singleton Constructor Called!")

    @classmethod
    def get_instance(cls):
        with cls._lock:  # Ensure only one thread creates the instance
            if cls._instance is None:
                cls._instance = Singleton()
        return cls._instance


# Example usage
s1 = Singleton.get_instance()
s2 = Singleton.get_instance()

print(s1 == s2)  # True
