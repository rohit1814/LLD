# ✅ Key points:
# threading.Lock in Python replaces C++ std::mutex.
# __new__ is overridden (not __init__) since it controls object creation.
# The double check ensures the constructor is called only once, even with multiple threads.

import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()  # class-level lock for thread safety

    def __new__(cls):
        # First check (without locking)
        if cls._instance is None:
            with cls._lock:  # Lock only if needed
                # Second check (inside lock)
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__new__(cls)
                    print("Singleton Constructor Called!")
        return cls._instance


# Example usage
s1 = Singleton()
s2 = Singleton()

print(s1 == s2)  # True


