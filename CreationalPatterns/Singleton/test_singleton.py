"""Module that contains the example of singleton design pattern"""

import unittest
from singleton import Singleton


class TestSingleton(unittest.TestCase):
    """Test Singleton design pattern"""

    def test_should_be_same_instance(self):
        """Test that objects are the same instance"""
        x = Singleton()
        y = Singleton()
        self.assertIs(x, y)

    def test_shuld_return_result_of_operation(self):
        """Test operation return"""
        x = Singleton()
        self.assertEqual(x.operation(), "Singleton operation")


if __name__ == "__main__":
    unittest.main()
