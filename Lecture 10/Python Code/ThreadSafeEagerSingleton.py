# It simplifies the singleton pattern by creating the instance at the time of class loading.
# This approach is inherently thread-safe since the instance is created before any thread accesses it.
# However, it may lead to resource wastage if the instance is never used.

class Singleton:
    _instance = None

    def __init__(self):
        print("Singleton Constructor Called!")

    @classmethod
    def get_instance(cls):
        return cls._instance


# Eager initialization (instance created when class is defined)
Singleton._instance = Singleton()

# Example usage
s1 = Singleton.get_instance()
s2 = Singleton.get_instance()

print(s1 == s2)  # True
