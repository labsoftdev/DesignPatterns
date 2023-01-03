"""This module contains the prototype interface for the Prototype design pattern."""
from __future__ import annotations


class Prototype:
    """The prototype interface declares methods for cloning itself."""

    def clone(self) -> Prototype:
        """Clone a prototype"""

    def operation(self):
        """Do something..."""
