class Pet:
    def __init__(self, aName, aAge):
        self.name = aName; self.age = aAge
    
    def makeSound(self):
        print("I do not know what sound to make!")
        
class Dog(Pet): #inheriting from parent class Pet
    def makeSound(self):
        print("I am a dog and I bark!")
        
class Cat(Pet): #inheriting from parent class Pet
    def makeSound(self):
        print("I am a cat and I Meow!")
        
class Fish(Pet): #inheriting from parent class Pet
    pass
    
d = Dog("Tim", 25); d.makeSound()
c = Cat("Blues", 20); c.makeSound()
f = Fish("Bubbles", 10); f.makeSound()