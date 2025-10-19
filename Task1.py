from abc import ABC, abstractmethod
from functools import reduce
# Class Object constructor
print("-"*40)


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print(f"Name: {self.name}, Roll: {self.roll}")


name = input("enter your name:") 
roll = int(input("enter your roll:"))
s1 = Student(name, roll)
s1.show()
print("-"*40)

# Instance, Class, Static method


class Example:
    course = "Python"

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name: {self.name}")

    @classmethod
    def cls_info(cls):
        print(f"This is a {cls.course} class")

    @staticmethod
    def greet():
        print("Welcome to Python class!")


obj = Example("Saloni")
obj.show()
Example.cls_info()
Example.greet()
print("-"*40)

# Inheritance


class Parent:
    def display(self):
        print("This is parent class")


class Child(Parent):
    def show(self):
        print("This is child class")


c = Child()
c.display()
c.show()
print("-"*40)

# polymorphism


class Bird:
    def sound(self):
        print("Some generic sound")


class Sparrow(Bird):
    def sound(self):
        print("Chirp Chirp")


class Crow(Bird):
    def sound(self):
        print("Caw Caw")


for bird in [Sparrow(), Crow()]:
    bird.sound()
print("-"*40)

# Encapsulation


class Bank:
    def __init__(self):
        self.__balance = 0  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


b = Bank()
b.deposit(1000)
print(b.get_balance())
print("-"*40)

# Abstraction


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


c = Circle(5)
print(c.area())
print("-"*40)

# Decorators


def decorator_func(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


@decorator_func
def say_hello():
    print("Hello, World!")


say_hello()
print("-"*40)

#  Generator


def numbers():
    for i in range(1, 6):
        yield i


for n in numbers():
    print(n)
print("-"*40)

# list Comprehension

Squares = [x**2 for x in range(5)]
print(Squares)

# dictionary comprehension

dic = {x: x**2 for x in range(5)}
print(dic)


# Set comprehension

nums = {x for x in [1, 2, 2, 3, 3, 4]}
print(nums)
print("-"*40)

# lambda, map, Filter,Reduce

nums = [1, 2, 3, 4]

# Lambda + maps
square = list(map(lambda x: x**2, nums))
print(square)

# Filter
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)

# Reduce
sum_all = reduce(lambda a, b: a + b, nums)
print(sum_all)
print("-"*40)