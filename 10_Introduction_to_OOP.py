# Introduction to Object-Oriented Programming (OOP)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# Creating an Object
person = Person("Alice", 25)
print(person.greet())
