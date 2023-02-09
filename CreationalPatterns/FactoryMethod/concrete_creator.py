"""This module contains concrete implementations of Creator"""

from creator import Creator
from concrete_product import ConcreteProductA, ConcreteProductB


class ConcreteCreator(Creator):
    """A concrete class for a creator."""

    def factory_method_a(self):
        return ConcreteProductA()

    def factory_method_b(self):
        return ConcreteProductB()
