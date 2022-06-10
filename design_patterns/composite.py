################################################################################
#
# Program: Composite Design Pattern
# 
# Description: An implementation of the composite design pattern in Python. See 
# the Wikipedia article for more information on the design pattern: 
#   https://en.wikipedia.org/wiki/Composite_pattern
# The core idea behind the pattern is that we can treat a single object the same
# as a group (or 'composition') of objects with respect to some operation (or 
# multiple operations).  The single object is a 'leaf' and the group of objects 
# is a 'composite', and the common operation (or operations) is defined by an 
# interface 'component'.  In our example, we use the pattern to model a file 
# system, with files as our leaf objects, folders as our composite objects, and 
# our component interface will have these objects implement a size operation.
#
# YouTube Lesson: https://www.youtube.com/watch?v=Y4GjKII_YDQ 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Import the abstract base class module so we can make the component class 
# an abstract base class.
from abc import ABC, abstractmethod

# We make Component a derived class of ABC to make it an abstract base class, 
# and we define size as an abstract method using the @abstract method 
# decorator.  Our File and Folder classes will be derived classes of Component 
# that must provide an implementation of this size method.
class Component(ABC):

  @abstractmethod 
  def size(self):
    pass 

# Files are a derived class of Component and so must implement the size method,
# File objects will be the 'leaf objects' in our implementation of the pattern.
class File(Component):
  
  # File objects will be given a name and size when they are instantiated
  def __init__(self, name, size):
    self.__name = name 
    self.__size = size 
  
  # As a File is a 'leaf object' it's size operation is simple, it simply 
  # returns its size
  def size(self):
    return self.__size 

# Folder objects are also a derived class of Component and so must also 
# provide an implementation for the size method.  The Folder objects are 
# the 'composite objects' in our implementation of the pattern, and so may 
# have children that are other components (i.e. the files and subfolders of 
# a folder).
class Folder(Component):
  
  # When a Folder object is instantiated it will be given a name and a list of 
  # components, the components are the 'children' of the Folder
  def __init__(self, name, components):
    self.__name = name 
    self.__components = components 
  
  # Our Folder 'composite' object has a more complicated job to return its size,
  # it must sum and return the size of all of its children (note the children 
  # could be File objects AND/OR Folder objects).
  def size(self):
    total = 0
    for component in self.__components:
      total += component.size()
    return total 
  
  # Variations and extensions of the Composite pattern allow for methods that 
  # let Composite objects manage their children, e.g. by adding or removing 
  # children.  Here we implement an add method that adds a new component (child)
  # to the list of components.
  def add(self,component):
    self.__components.append(component)


# Create 3 File objects to represent a resume, cover letter and reference letter
resume = File("resume.doc", 1024)
cover_letter = File("cover.doc", 2048)
reference = File("reference.pdf", 4096)

# Create a 'Documents' Folder object that contains these 3 files as children
documents = Folder("Documents", [resume, cover_letter, reference])

# Create 2 File objects to represent a todo list and screenshot
todo = File("todo.txt", 256)
screenshot = File("screenshot.png", 25000)

# Create a 'Desktop' Folder object that contains these 2 files as children
desktop = Folder("Desktop", [todo, screenshot])

# Create a 'User' Folder object that contains the Desktop and Documents folders 
# as children (remember Folder objects may contain Folder objects as children)
user = Folder("User", [desktop, documents])

#  As of this point in our code, we will have built a tree-structure of Folder
#  and File objects that looks like this...
#
#                todo.txt
#               /
#        Desktop
#       /       \
#      /         screenshot.png
#  User            
#      \            resume.doc
#       \          /
#        Documents - cover.doc
#                  \
#                   reference.pdf

# We can use the size method whether the object is a File or Folder
print(resume.size())
print(documents.size())
print(desktop.size())
print(user.size())

# Create a new file to represent secret death star plans
death_star_plans = File("secret.txt", 512)

# Use the add method to add this plan to the User folder
user.add(death_star_plans)

# We can see that the size of the User folder will have increased by 512 after
# adding the secret death star plans to the folder 
print(user.size())

# Create a list of Components that include both File and Folder objects
components = [todo, user, screenshot]

# We can use the size method with ALL objects in this list because we know all 
# Component objects be they File or Folder objects will support the 'size 
# operation'
for component in components:
  print(component.size())
