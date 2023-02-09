"""This module contains implementation and example of Singleton design pattern"""


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

    def operation(self):
        return "Singleton operation"
