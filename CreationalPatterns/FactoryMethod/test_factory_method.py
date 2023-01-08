"""This module contains example of Factory methods design pattern"""
import unittest
from concrete_creator import ConcreteCreator
from product import Product


class TestFactoryMethod(unittest.TestCase):
    """Tests for Factory methods design pattern"""

    def setUp(self) -> None:
        self.creator = ConcreteCreator()

    def test_should_create_product_objects(self):
        """Test that creator returns a Product object implementing the factory method"""
        product_a = self.creator.factory_method_a()
        product_b = self.creator.factory_method_b()
        self.assertIsInstance(product_a, Product)
        self.assertIsInstance(product_b, Product)

    def test_should_return_results_of_product_a_operations(self):
        """Test result of productA operations"""
        product_a = self.creator.factory_method_a()
        self.assertEqual(
            product_a.operation_a(), "I am product A executing operation A"
        )
        self.assertEqual(
            product_a.operation_b(), "I am product A executing operation B"
        )

    def test_should_return_results_of_product_b_operations(self):
        """Test result of productB operations"""
        product_b = self.creator.factory_method_b()
        self.assertEqual(
            product_b.operation_a(), "I am product B executing operation A"
        )
        self.assertEqual(
            product_b.operation_b(), "I am product B executing operation B"
        )


if __name__ == "__main__":
    unittest.main()
