"""Module that contains the example of singleton design pattern"""

import unittest
from singleton import Singleton


class TestSingleton(unittest.TestCase):
    """Test Singleton design pattern"""

    def test_should_be_same_instance(self):
        """Test that objects are the same instance"""
        _x = Singleton()
        _y = Singleton()
        self.assertIs(_x, _y)

    def test_shuld_return_result_of_operation(self):
        """Test operation return"""
        _x = Singleton()
        self.assertEqual(_x.operation(), "Singleton operation")


if __name__ == "__main__":
    unittest.main()
