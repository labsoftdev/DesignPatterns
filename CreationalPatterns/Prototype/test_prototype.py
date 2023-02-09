"""This module contains example of prototype design pattern"""
import unittest
from concrete_prototype import ConcretePrototype1, ConcretePrototype2


class TestPrototype(unittest.TestCase):
    """Test prototype design pattern"""

    def setUp(self) -> None:
        self.prototype1 = ConcretePrototype1("hello", 123)
        self.prototype2 = ConcretePrototype2("world", 456, [1, 2, 3])

    def test_should_have_different_instances(self):
        """Test that the prototypes are not the same object as the instances"""
        instance1 = self.prototype1.clone()
        instance2 = self.prototype2.clone()
        self.assertIsNotNone(instance1, self.prototype1)
        self.assertIsNotNone(instance2, self.prototype2)

    def test_should_have_the_same_field_values(self):
        """Test that the prototype and instance have the same field values"""
        instance1 = self.prototype1.clone()
        instance2 = self.prototype2.clone()
        self.assertEqual(instance1.operation(), self.prototype1.operation())
        self.assertEqual(instance2.operation(), self.prototype2.operation())


if __name__ == "__main__":
    unittest.main()
