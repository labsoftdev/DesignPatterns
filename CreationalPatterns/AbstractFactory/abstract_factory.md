# Abstract Factory
The Abstract Factory is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes.

## Intent
- Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
- The factory pattern separates the creation of objects from their implementation.

## Problem
- A system should be independent of how its objects are created, composed, and represented.
- A system should be configured with one of multiple families of objects.
- You want to provide a class library of objects, and you want to reveal just their interfaces, not their implementations.

## Solution
Define an interface for creating an object, but let subclasses decide which class to instantiate. The factory method lets a class defer instantiation to subclasses.

## Participants
- **AbstractFactory**: declares an interface for operations that create abstract product objects.
- **ConcreteFactory**: implements the operations to create concrete product objects.
- **AbstractProduct**: declares an interface for a type of product object.
- **Product**: defines a product object to be created by the corresponding concrete factory, implements the AbstractProduct interface.

## Related Design Patterns
AbstractFactory classes are often implemented with factory methods (Factory
Method Design Pattern), but they can also be implemented using Prototype Design Pattern.
A concrete factory is often a singleton (Singleton Design Pattern).
