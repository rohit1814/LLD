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



## Other way of creating singleton
# https://www.geeksforgeeks.org/python/singleton-pattern-in-python-a-complete-guide/

class SingletonClass(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(SingletonClass, cls).__new__(cls)
    return cls.instance
  
singleton = SingletonClass()
new_singleton = SingletonClass()

print(singleton is new_singleton)

singleton.singleton_variable = "Singleton Variable"
print(new_singleton.singleton_variable)