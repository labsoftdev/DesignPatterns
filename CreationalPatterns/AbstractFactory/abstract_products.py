"""Each distinct product of a product family should have a base interface."""

from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    """
    All variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        """
        Product A is able to do something...
        """

    @abstractmethod
    def another_useful_function_a(self) -> str:
        """
        Product A is able to do something else...
        """


class AbstractProductB(ABC):
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """

    @abstractmethod
    def useful_function_b(self) -> None:
        """
        Product B is able to do its own thing...
        """

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
