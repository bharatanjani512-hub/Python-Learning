# Creating a class
class Student:
    
    # Constructor (initializes object)
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    # Method to display student details
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


# Creating an object of the class
student1 = Student("Anjani", 24, 95)

# Calling method using object
student1.display()