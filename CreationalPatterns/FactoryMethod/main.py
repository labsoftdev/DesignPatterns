"""This module contains example of Factory methods design pattern"""
from concrete_creator import ConcreteCreator


def main() -> None:
    """Creating objects using Factory methods and performing operations"""
    creator = ConcreteCreator()
    product_a = creator.factory_method_a()
    product_b = creator.factory_method_b()

    print(product_a.operation_a() + " AND " + product_b.operation_a())
    print(product_a.operation_b() + " AND " + product_a.operation_b())


if __name__ == "__main__":
    main()
