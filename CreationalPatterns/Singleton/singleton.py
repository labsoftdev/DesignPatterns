class Singleton:
    """
    A class that ensures that only one instance of itself can be created.
    Provides a global access point to the instance.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    """
    A class that is a singleton.
    """

    def __new__(cls, arg1, arg2, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, arg1, arg2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arg1 = arg1
        self.arg2 = arg2


x = MyClass(1, 2)
y = MyClass(3, 4)

"""Checks that x and y are the same instance."""
assert x is y
