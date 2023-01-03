"""This module contains the Product class."""


class Product:
    """Represents the complex object being built."""

    def __init__(self):
        """Initialize a new instance of the Product class."""
        self.parts = []

    def add(self, part):
        """Add a part to the product."""
        self.parts.append(part)

    def list_parts(self):
        """List the parts of the product."""
        print(f"Product parts: {', '.join(self.parts)}", end="")
