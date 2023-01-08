"""This module contains concrete products"""

from product import Product


class ConcreteProductA(Product):
    """A concrete class for a product."""

    def operation_a(self):
        return "I am product A executing operation A"

    def operation_b(self):
        return "I am product A executing operation B"


class ConcreteProductB(Product):
    """A concrete class for a product."""

    def operation_a(self):
        return "I am product B executing operation A"

    def operation_b(self):
        return "I am product B executing operation B"
