# Builder
The Builder design pattern is a creational design pattern that allows for the construction of complex objects step by step. The pattern separates the construction of an object from its representation, so that the same construction process can create different representations.

## Intent
The intent of the Builder design pattern is to separate the construction of a complex object from its representation, so that the same construction process can create different representations. This allows for greater flexibility in creating objects, as the construction process can be reused to create different representations of the object.

## Problem
Suppose you want to create a complex object, such as a car, that has many parts and can be assembled in different ways. Creating such an object directly would be inflexible and error-prone, as you would need to specify all of the parts and how they fit together in a single constructor. This would make it difficult to change the object's representation without changing the code that creates it.

## Solution
The Builder design pattern solves this problem by separating the construction of the object from its representation. It does this by defining an abstract ***Builder*** interface that specifies methods for creating the parts of the object, and a ***ConcreteBuilder*** class that provides an implementation of these methods. A ***Director*** class is responsible for constructing the object using the ***Builder*** interface.

This allows the same construction process to be used to create different representations of the object. The ***ConcreteBuilder*** class keeps track of the representation it is creating, and the ***Product*** class represents the complex object being built.

By using the Builder design pattern, you can create complex objects in a flexible and reusable way, without the need to specify all of the details of the object's representation in a single constructor.

## Participants
- **Director**: Constructs an object using the Builder interface.
- **Builder**: Specifies an abstract interface for creating parts of a Product object.
- **ConcreteBuilder**: Constructs and assembles parts of the product by implementing the Builder interface. Defines and keeps track of the representation it creates.
- **Product**: Represents the complex object being built.

## Related Design Patterns
***Abstract Factory*** is similar to Builder in that it too may construct complex
objects. The primary difference is that the Builder pattern focuses on constructing a
complex object step by step. Abstract Factory's emphasis is on families of product
objects (either simple or complex). Builder returns the product as a final step, but as far as the Abstract Factory pattern is concerned, the product gets returned
immediately.
A ***Composite*** is what the builder often builds.
