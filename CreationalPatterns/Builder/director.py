"""
This module contains the Director class.
"""


class Director:
    """Constructs an object using the Builder interface."""

    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        """Construct the object by calling the build methods of the builder."""
        self._builder.build_part_a()
        self._builder.build_part_b()
        self._builder.build_part_c()

    def get_builder(self):
        """Returns the builder that has been constructed."""
        return self._builder
