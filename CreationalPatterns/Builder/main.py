"""This module contains example of Builder design pattern"""

from concrete_builder import ConcreteBuilder
from director import Director


def main() -> None:
    """
    Construct a product using the Builder design pattern.
    """
    builder = ConcreteBuilder()
    director = Director(builder)
    director.construct()
    product = builder.get_product()
    product.list_parts()


if __name__ == "__main__":
    main()
