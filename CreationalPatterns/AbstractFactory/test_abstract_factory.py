"""Module for testing examples of AbstractFactory design pattern"""

import unittest
from typing import Type
from concrete_factories import ConcreteFactory1, ConcreteFactory2
from abstract_factory import AbstractFactory
from abstract_products import AbstractProductA, AbstractProductB


def create_factory(factory_type: Type[AbstractFactory]) -> AbstractFactory:
    """Creating a factory from a concrete factory"""
    return factory_type()


class TestAbstractFactory(unittest.TestCase):
    """Class for testing AbstractFactory design pattern"""

    def setUp(self):
        self.factory1 = create_factory(ConcreteFactory1)
        self.factory2 = create_factory(ConcreteFactory2)

    def test_should_receive_a_factory_object_of_the_specified_type(self):
        """Test that created factory objects extends the AbstractFactory"""
        self.assertIsInstance(self.factory1, AbstractFactory)
        self.assertIsInstance(self.factory2, AbstractFactory)

    def test_should_receive_an_object_of_the_abstract_product_a(self):
        """Test that created products are objects which implement AbstractProductA"""
        product_a1 = self.factory1.create_product_a()
        product_a2 = self.factory2.create_product_a()
        self.assertIsInstance(product_a1, AbstractProductA)
        self.assertIsInstance(product_a2, AbstractProductA)

    def test_should_receive_an_object_of_the_abstract_product_b(self):
        """Test that created products are objects which implement AbstractProductB"""
        product_b1 = self.factory1.create_product_b()
        product_b2 = self.factory2.create_product_b()
        self.assertIsInstance(product_b1, AbstractProductB)
        self.assertIsInstance(product_b2, AbstractProductB)

    def test_should_receive_results_of_the_concrete_product_a_methods(self):
        """Testing returns of the results of the ConcreteProductA methods"""
        product = self.factory1.create_product_a()
        self.assertEqual(product.useful_function_a(), "The result of the product A1.")
        self.assertEqual(
            product.another_useful_function_a(), "The another result of the product A1."
        )

    def test_should_receive_results_of_the_concrete_product_b_methods(self):
        """Testing returns of the results of the ConcreteProductB methods"""
        product = self.factory1.create_product_b()
        product_a = self.factory1.create_product_a()
        self.assertEqual(product.useful_function_b(), "The result of the product B1.")
        self.assertEqual(
            product.another_useful_function_b(product_a),
            "The result of the B1 collaborating with the (The result of the product A1.)",
        )


if __name__ == "__main__":
    unittest.main()
