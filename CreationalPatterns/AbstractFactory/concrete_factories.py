"""Implementations of concrete factories"""

from abstract_factory import AbstractFactory
from concrete_products import (
    ConcreteProductA1,
    ConcreteProductB1,
    ConcreteProductA2,
    ConcreteProductB2,
)


class ConcreteFactory1(AbstractFactory):
    """Concrete factory for creating concrete products"""

    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """Concrete factory for creating concrete products"""

    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()

    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()
