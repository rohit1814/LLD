class NoSingleton:
    def __init__(self):
        print("Constructor called. New Object created.")


# Example usage
s1 = NoSingleton()
s2 = NoSingleton()

print(s1 == s2)  # False, because they are two different objects
