"""This module contains abstract Creator class"""

from abc import ABC, abstractmethod


class Creator(ABC):
    """An abstract base class for creating objects."""

    @abstractmethod
    def factory_method_a(self):
        """Create an object of the Product class."""

    @abstractmethod
    def factory_method_b(self):
        """Create an object of the Product class."""
