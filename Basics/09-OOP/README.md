# 09. Object-Oriented Programming (OOP) 🐍

## 📖 Overview

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into classes and objects. It helps create reusable, modular, and maintainable programs by modeling real-world entities.

---

## 🎯 Learning Objectives

After completing this topic I should be able to:

- Understand classes and objects
- Create constructors
- Define methods
- Apply inheritance
- Understand encapsulation
- Learn polymorphism and abstraction

---

## 📚 Topics Covered

- Class
- Object
- Constructor (`__init__`)
- Methods
- Inheritance
- Encapsulation
- Polymorphism
- Abstraction

---

## 💻 Example

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)

student = Student("Anjani")
student.display()
```

---

## 🔑 Key Takeaways

- Classes are blueprints for objects.
- Objects are instances of classes.
- Constructors initialize object data.
- OOP promotes code reusability and organization.

---

## 📌 Status

✅ Completed