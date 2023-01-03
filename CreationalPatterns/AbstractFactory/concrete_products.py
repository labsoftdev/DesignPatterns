"""Implementation of concrete products"""

from abstract_products import AbstractProductA, AbstractProductB


class ConcreteProductA1(AbstractProductA):
    """Concrete product A1."""

    def useful_function_a(self) -> str:
        return "The result of the product A1."

    def another_useful_function_a(self) -> str:
        return "The another result of the product A1."


class ConcreteProductA2(AbstractProductA):
    """Concrete product A2."""

    def useful_function_a(self) -> str:
        return "The result of the product A2."

    def another_useful_function_a(self) -> str:
        return "The another result of the product A2."


class ConcreteProductB1(AbstractProductB):
    """Concrete product B1."""

    def useful_function_b(self) -> str:
        return "The result of the product B1."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    """Concrete product B2."""

    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.another_useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"
