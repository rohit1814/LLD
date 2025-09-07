class Singleton:
    _instance = None   # class-level variable

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            print("Singleton Constructor called")
        return cls._instance


# Example usage
s1 = Singleton()
s2 = Singleton()

print(s1 == s2)  # True, both are the same instance
