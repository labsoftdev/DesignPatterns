"""This module contains example of Builder design pattern"""
import unittest
from concrete_builder import ConcreteBuilder
from director import Director


class TestBuilder(unittest.TestCase):
    """Tests for the Builder design pattern."""

    def test_should_return_builded_product(self):
        """Test that a product can be created using the Builder pattern."""
        builder = ConcreteBuilder()
        director = Director(builder)
        director.construct()
        product = builder.get_product()
        self.assertEqual(product.parts, ["Part A", "Part B", "Part C"])
        product.list_parts()


if __name__ == "__main__":
    unittest.main()
