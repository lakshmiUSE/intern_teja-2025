class Teacher:
    def teach(self):
        print("teaches the python")
#parent 2 class
class Coach(Teacher):
    def train(self):
        print("trains a game")
#child class inherites from both teacher and coach
class Student(Teacher):
    def display(self):
        print("learns the study")

s1=Student()
s1.teach()

s1.display()

s2=Coach()
s2.train()
s2.teach()
