"""This module contains the ConcreteBuilder class."""

from builder import Builder
from product import Product


class ConcreteBuilder(Builder):
    """
    Constructs and assembles parts of the product by implementing the Builder
    interface. Defines and keeps track of the representation it creates.
    """

    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("Part A")

    def build_part_b(self):
        self.product.add("Part B")

    def build_part_c(self):
        self.product.add("Part C")

    def get_product(self):
        """Get the product that has been built."""
        return self.product
