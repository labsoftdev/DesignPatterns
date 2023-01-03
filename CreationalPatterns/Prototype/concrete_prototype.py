"""This module contains implementations of concrete prototypes"""


from copy import deepcopy
from prototype import Prototype


class ConcretePrototype1(Prototype):
    """
    Concrete Prototypes implement cloning by copying field values.
    """

    def __init__(self, field1: str, field2: int) -> None:
        self._field1 = field1
        self._field2 = field2

    def clone(self) -> Prototype:
        return deepcopy(self)

    def operation(self):
        return self._field1 + " " + str(self._field2)


class ConcretePrototype2(Prototype):
    """
    Different concrete prototypes may have different cloning implementations.
    """

    def __init__(self, field1: str, field2: int, field3: list) -> None:
        self._field1 = field1
        self._field2 = field2
        self._field3 = field3

    def clone(self) -> Prototype:
        return ConcretePrototype2(self._field1, self._field2, self._field3[:])

    def operation(self):
        return self._field1 + " " + str(self._field2) + " " + str(self._field3)
