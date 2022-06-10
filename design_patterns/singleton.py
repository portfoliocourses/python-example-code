################################################################################
#
# Program: Singleton Design Pattern Tutorial
# 
# Description: Two examples of how to implement the singleton pattern in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=CukrRuOAVqg
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# APPROACH #1 - getInstance() method
#
# Client code uses Singleton1.getInstance() to retrieve object instance, it 
# should never use Singleton1().  This makes it much more explicit that the 
# object is a singleton, but it's also not the usual way we create an object.
#

class Singleton1:

  # class variable __instance will keep track of the lone object instance
  __instance = None 

  # staticmethod getInstance is associated with the Singleton1 class as opposed
  # to a particular object instance (note the lack of 'self' parameter).  The 
  # method checks to see if the instance has been created yet and if it has not 
  # it create the object, either way it returns the instance.
  @staticmethod 
  def getInstance():
    if Singleton1.__instance == None:
      Singleton1()
    return Singleton1.__instance

  # This is a constructor-like magic method / dunder method that is called when 
  # an object is instantiated.  The object sets the class variable __instance to
  # the object instance.  Singleton1() should only ever be called *once* and by 
  # the getInstance() method in this implementation of the pattern, and so if 
  # this method is ever executed when __instance is NOT none, it means that 
  # client code must be attempting to use Singleton1() directly (which we don't
  # want), and so we raise an Exception if this is the case. 
  def __init__(self):
    if Singleton1.__instance != None:
       raise Exception("Singleton object already created!")
    else:
       Singleton1.__instance = self

# We call getInstance to get the Singleton1 instance... in the case of s1 it 
# will need to be created, in the case of s2, the same instance is simply 
# returned!  Notice how s1 = s2 when we print them.
s1 = Singleton1.getInstance()
print(s1)
s2 = Singleton1.getInstance()
print(s2)

# if we set an attribute on s1, s2 will have the same value because they 
# both refer to the same object
s1.x = 5
print(s2.x)


# APPROACH #1 - Singleton2() method
#
# Client code uses Singleton2() to create AND access the Singleton2 instance,
# which is the standard way in which an object is created.  This makes it more 
# implicit that Singleton2 is in fact a Singleton object... the writer of the 
# client code might not be aware that Singleton2 is a singleton (perhaps it is
# not in the name of the class as it is here), and may expect that Singleton2() 
# returns a new object each time it is used as would normally be expected!
#

class Singleton2:

  # class variable __instance will keep track of the lone object instance
  __instance = None 

  # A magic method / dunder method that is called when we create a Singleton2 
  # object with Singleton2().  We have it check the __instance class variable 
  # to see if the instance has been created, if it hasn't, we create it, and 
  # whether we needed to create it or not we return the instance.
  def __new__(cls):

    if (cls.__instance is None):

      cls.__instance = \
        super(Singleton2, cls).__new__(cls)
    
    return cls.__instance 

# We can just create the Singleton2 objects in the usual way, but it is only 
# ever going to be the same object that is returned as s1 = s2!
s1 = Singleton2()
print(s1)
s2 = Singleton2()
print(s2)

# again if we set an attribute on s1, s2 will have the same value because they 
# both refer to the same object
s1.x = 5
print(s2.x)
