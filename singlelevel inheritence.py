#single level inheritence

class Person:
    def display(self):
        print("teja")
class Student(Person):
    def course(self):
        print("python")

s1=Student()
s1.display()
s1.course()
