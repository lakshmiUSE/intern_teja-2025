#polymorphism

#many forms

#it allows the same function method or operater to behave
#differently depending on the object data type it is working with

class Dog:
    def sound(self):
        return "bark"
class Cat:
    def sound(self):
        return "meow"

#example of polymarphism

for animal in(Dog(),Cat()):
    print(animal.sound())
    
