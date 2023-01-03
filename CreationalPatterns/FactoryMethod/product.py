"""This module contains abstract class Product"""

from abc import ABC, abstractmethod


class Product(ABC):
    """An abstract base class for objects."""

    @abstractmethod
    def operation_a(self):
        """Perform an operation A."""

    @abstractmethod
    def operation_b(self):
        """Perform an operation B."""
