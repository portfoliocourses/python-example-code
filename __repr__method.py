################################################################################
#
# Program: __repr__ Method Example
# 
# Description: Example of using the __repr__ magic method (i.e. dunder method)
# in Python to represent an object as a string in a formal, complete way that is
# suitable for debugging or programming purposes.
#
# YouTube Lesson: https://www.youtube.com/watch?v=LV27ZMm8TWk 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A simple class for representing students
class Student:

    # Student objects will have name and grade attributes
    def __init__(self, name, grade):
        self.name = name 
        self.grade = grade 

    # The __repr__ method is expected to return a string representation of the 
    # object that is suitable for programming or debugging purposes.  Here we 
    # use an f-string to build and return a string that contains the object 
    # member variable values with the format: Student('name','grade')
    def __repr__(self):
        return f"Student('{self.name}','{self.grade}')"

    # There is a similar magic method called __str__ that is intended for 
    # representing the object as a string in a more informal and human-readable
    # way.  We could also define this method.
    #
    # def __str__(self):


# Create a Student object
mary = Student("Mary", "A+")

# The built-in repr() function will call our __repr__ method above and return 
# the string it produces, which we output...
mary_string = repr(mary)
print(mary_string)

# The string returned be our __repr__ method can be evaluated as Python code 
# using the built in eval() function, which will create a Student object.  
# We assign the resulting object to mary_object and verify it's type and 
# output the attribute name. 
mary_object = eval(mary_string)
print(type(mary_object))
print(mary_object.name)

# If we do not define an __str__ method, the print() function will use our 
# __repr__ method to convert mary_object to a string to be printed.
print(mary_object)