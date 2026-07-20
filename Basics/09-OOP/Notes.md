# Object-Oriented Programming (OOP) Notes

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into **classes** and **objects**. It helps build scalable, reusable, and maintainable applications.

Python supports OOP through classes, objects, inheritance, polymorphism, encapsulation, and abstraction.

---

# Why OOP?

OOP helps us:

- Organize code into reusable components
- Reduce code duplication
- Improve readability
- Model real-world entities
- Simplify maintenance of large projects

---

# Class

A **class** is a blueprint for creating objects.

### Syntax

```python
class Student:
    pass
```

### Example

```python
class Student:
    name = "Anjani"

student1 = Student()

print(student1.name)
```

---

# Object

An **object** is an instance of a class.

### Example

```python
class Car:
    brand = "Toyota"

car1 = Car()
car2 = Car()

print(car1.brand)
print(car2.brand)
```

---

# Constructor (`__init__`)

A constructor initializes object attributes automatically when an object is created.

### Example

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Anjani", 22)

print(student.name)
print(student.age)
```

---

# Methods

Methods are functions defined inside a class.

### Example

```python
class Student:

    def greet(self):
        print("Welcome!")

student = Student()

student.greet()
```

---

# Inheritance

Inheritance allows one class to inherit the properties and methods of another class.

### Example

```python
class Animal:

    def speak(self):
        print("Animal speaks")

class Dog(Animal):

    def bark(self):
        print("Dog barks")

dog = Dog()

dog.speak()
dog.bark()
```

---

# Encapsulation

Encapsulation combines data and methods into a single unit while restricting direct access to certain data.

### Example

```python
class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def show_balance(self):
        print(self.__balance)

account = BankAccount()

account.show_balance()
```

---

# Polymorphism

Polymorphism allows different classes to define methods with the same name but different implementations.

### Example

```python
class Bird:

    def sound(self):
        print("Bird chirps")

class Dog:

    def sound(self):
        print("Dog barks")

animals = [Bird(), Dog()]

for animal in animals:
    animal.sound()
```

---

# Abstraction

Abstraction hides implementation details and exposes only the necessary functionality.

### Example

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

square = Square(5)

print(square.area())
```

---

# Four Pillars of OOP

| Pillar | Purpose |
|---------|---------|
| Encapsulation | Protects data |
| Abstraction | Hides implementation |
| Inheritance | Reuses code |
| Polymorphism | Allows one interface with multiple implementations |

---

# Real-world Example

Imagine a **Car**.

- Class → Car
- Object → My Honda City
- Attributes → Color, Model, Speed
- Methods → Start(), Stop(), Accelerate()

A class defines what a car is, while each object represents a specific car.

---

# Key Notes

- A class is a blueprint for objects.
- An object is an instance of a class.
- Constructors initialize object data.
- Methods define object behavior.
- Inheritance promotes code reuse.
- Encapsulation protects data.
- Polymorphism enables flexibility.
- Abstraction simplifies complex systems.

---

# Summary

| Concept | Purpose |
|---------|---------|
| Class | Blueprint for objects |
| Object | Instance of a class |
| Constructor | Initializes object attributes |
| Method | Function inside a class |
| Inheritance | Reuse code from another class |
| Encapsulation | Protect data |
| Polymorphism | Multiple implementations |
| Abstraction | Hide unnecessary details |