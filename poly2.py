class Dog:
    def sound(self):
        return "bark"
class Cat(Dog):
    def sound(self):
        return "meow"
obj2=Dog()
obj1=Cat()
print(obj1.sound())
print(obj2.sound())
