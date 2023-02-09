# Adapter Design Pattern
The Adapter design pattern is a structural pattern that allows objects with incompatible interfaces to collaborate. It translates the calls to the interface required by a client into calls to the objects that the client expects.

## Intent
- Convert the interface of a class into another interface clients expect.
- Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.
- The pattern is used when existing classes have the functionality required by a new system but their interfaces don't match the interfaces required by the new system.
  
## Problem
- You want to reuse existing classes that don't have the required interface.
- You want to create a reusable class that cooperates with unrelated or unforeseen classes.
- A class has some abilities that another class requires, but the two classes have incompatible interfaces.
  
## Solution
Create a wrapper class that can be used by the client class as if it were the original class. The adapter class implements the required interface and translates calls from the client to the original class.

## Structure
Adapter Design Pattern

## Participants
- **Target**: defines the domain-specific interface that Client uses.
- **Client**: collaborates with objects conforming to the Target interface.
- **Adaptee**: defines an existing interface that needs adapting.
- **Adapter**: adapts the interface of Adaptee to the Target interface.
  
## Related Design Patterns
The Adapter design pattern is often used in combination with the Facade and Composite patterns.