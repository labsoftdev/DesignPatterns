"""Module for running examples of AbstractFactory design pattern"""

from typing import Type
from concrete_factories import ConcreteFactory1, ConcreteFactory2
from abstract_factory import AbstractFactory


def create_factory(factory_type: Type[AbstractFactory]) -> AbstractFactory:
    """Creating a factory from a concrete factory"""
    return factory_type()


def main() -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    factory1 = create_factory(ConcreteFactory1)
    product_a1 = factory1.create_product_a()
    product_b1 = factory1.create_product_b()

    print(product_b1.useful_function_b())
    print(product_b1.another_useful_function_b(product_a1))

    factory2 = create_factory(ConcreteFactory2)
    product_a2 = factory2.create_product_a()
    product_b2 = factory2.create_product_b()

    print(product_b2.useful_function_b())
    print(product_b2.another_useful_function_b(product_a2))


if __name__ == "__main__":
    main()
