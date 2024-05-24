#creating a basic class called Dog

#class Dog:
    #def makeSound(self):
        #print("Dog Barks!")

#d = Dog()
#d.makeSound()
#print(type(d))

#creating Dog class with some more complex methods
#herein we use the __init__() method and the self keyword argument
#you can relate the __init__() method as in contrast to constructor method in C++ which is called when an object is created
#the self keyword argument can be contrasted to the this pointer of C++ as it references the object which is being created/accessed
#and is passed to respective method functions implicitly (behind the scenes), just like this pointer

class Dog:
    def __init__(self, aName, aAge):
        self.name = aName
        self.age = aAge
    
    def displayNameAge(self):
        print("Dog name is - ", self.name)
        print("Dog age is - ", self.age)

d1 = Dog("Tim", 6)        
d2 = Dog("Alex", 7)

d1.displayNameAge(); print()
d2.displayNameAge()