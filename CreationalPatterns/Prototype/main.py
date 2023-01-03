"""This module contains example of prototype design pattern"""

from concrete_prototype import ConcretePrototype1, ConcretePrototype2


def main():
    """
    Demonstrates the use of the Prototype design pattern. Creates two prototype objects and
    uses the clone method to create two new instances. Verifies that the prototypes are not
    the same object as the instances and that the prototype and instance have the same field
    values.
    """

    prototype1 = ConcretePrototype1("hello", 123)
    prototype2 = ConcretePrototype2("world", 456, [1, 2, 3])

    # Use the prototype instances to create new objects
    instance1 = prototype1.clone()
    instance2 = prototype2.clone()

    # Verify that the prototypes are not the same object as the instances
    assert instance1 is not prototype1
    assert instance2 is not prototype2

    # Verify that the prototype and instance have the same field values
    assert instance1.operation() == prototype1.operation()
    assert instance1.operation() == prototype1.operation()


if __name__ == "__main__":
    main()
