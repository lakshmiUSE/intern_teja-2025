#__init__method

"""
__init__ method is special method wecan call it as a constucter
As a programer we no need to call explicity, the interpreter
will call this method at the time of object creation
"""


class Student:
    def __init__(self):
        print("inside a init method")
    def display(self):
        print("inside display method")



s1=Student()
s2=Student()
s3=Student()
s4=Student()
s1.display()
