"""1.Create a base class Person with attributes name and age, and a derived class Employee with an additional attribute salary.
 Display all the details using a method."""


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name,"age:",self.age)
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("salary:",self.salary)
        
e1=Employee("teju",23,45000)
e1.display()
        
"""2.Define two classes — Father and Mother — each having a method show().
Create a subclass Child that inherits from both and calls both show() methods."""
class Father:
    def display_father(self):
        print("father")
class Mother:
    def display_mother(self):
        print("mother")
class Child(Father,Mother):
    def display(self):
        print("child class")

c1=Child()
c1.display_father()
c1.display_mother()
c1.display()

"""3.Each class should have a method that prints information about its type.
 Create an object of ElectricCar and call all methods to show inheritance working."""

class Car:
    def type(self):
        print("Nomal car")
class ElectricCar(Car):
    def type(self):
        print("ElectricCar")

c1=ElectricCar()
c1.type()

