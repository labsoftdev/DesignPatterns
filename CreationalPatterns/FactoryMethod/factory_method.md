# Factory Method 
The factory method design pattern is a creational design pattern that provides an interface for creating objects in a super class, but allows subclasses to alter the type of objects that will be created.

## Intent
The intent of the factory method design pattern is to define an interface for creating an object, but let subclasses decide which class to instantiate. The factory method allows a class to defer instantiation to subclasses.

## Problem
Consider a situation where you have a super class with a method that returns an object of a certain type. However, the specific type of object that is returned can vary depending on the input.

In this case, you could use an if-else block or a switch statement to determine the specific type of object to return based on the input. However, this can make the code difficult to maintain and extend, as you need to update the if-else block or switch statement whenever you want to add a new type of object.

## Solution
To solve this problem, you can use the factory method design pattern. The factory method design pattern defines an interface for creating an object, but allows subclasses to alter the type of object that will be created.

In the factory method design pattern, the super class defines a factory method that takes a parameter that specifies the type of object to create. The factory class is responsible for creating the object, while the subclasses provide the implementation for the object that will be created.

This allows you to add new types of objects easily by simply creating a new subclass that provides an implementation for the object. The factory class does not need to be modified, as it relies on the subclasses to provide the implementation for the objects that it creates.

## Participants
- **Product**: Defines the interface of objects the factory method creates.
- **ConcreteProduct**: Implements the Product interface.
- **Creator**: Declares the factory method, which returns an object of type Product. Creator may also define a default implementation of the factory method that returns a default ConcreteProduct object.
May call the factory method to create a Product object.
- **ConcreteCreator**: Overrides the factory method to return an instance of a ConcreteProduct.
'''plantuml
@startuml 

abstract class Creator {
  - factory_method()
}

abstract class Product {
  - operation()
}

class ConcreteCreator {
  + factory_method()
}

class ConcreteProduct {
  + operation()
}

Client -down-> Creator: create creator object
Creator ---> Product: create product object
Client <-- Product: product objectS
Client --> Product: use product
@enduml


## Related Design Patterns
***Abstract Factory*** is often implemented with factory methods. The Motivation
example in the Abstract Factory pattern illustrates Factory Method as well.
Factory methods are usually called within ***Template Methods***. In the document example above, NewDocument is a template method.
***Prototypes*** don't require subclassing Creator. However, they often require
an Initialize operation on the Product class. Creator uses Initialize to initialize the
object. Factory Method doesn't require such an operation.