#multiple inheritence
#parent class1
class Teacher:
    def teach(self):
        print("teaches the python")
#parent 2 class
class Coach:
    def train(self):
        print("trains a game")
#child class inherites from both teacher and coach
class Student(Teacher,Coach):
    def display(self):
        print("learns the study")

s1=Student()
s1.teach()
s1.train()
s1.display()
