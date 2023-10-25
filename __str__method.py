################################################################################
#
# Program: __str__ Method Example
#
# Description: Example of using the __str__ method in Python which allows us to
# define an informal human-readable string representation of an object.
#
# YouTube Lesson: https://www.youtube.com/watch?v=GKFwko0byM0 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A simple class to represent students
class Student:
    
    # Initializes the attributes name and grade to the parameter values
    def __init__(self, name, grade):
        self.name = name 
        self.grade = grade 
    
    # If we define the magic method (i.e. dunder method) __str__ and have it
    # return a string, it is this string that will be used to represent the 
    # object with the built-in print(), str() and format() functions.  Here
    # we simply return the two attributes values in a string, using a f-string.
    def __str__(self):
        return f"{self.name} ({self.grade})"

    # Notably there is a similar function called __repr__ that is intended to
    # return a formal and complete representation of the object suitable for
    # debugging and developing purposes
    #  
    # def __repr__(self):


# Create a Student object
mary = Student("Mary", "A+")

# When we output the object with print the __str__ method we define will be 
# called and it is the string returned by this method that will be output.
# If we did not define __str__ the default string essentially will be the 
# object type + address.
print(mary)

# Our __str__ method will also be used if we call the built in str() function
mary_string = str(mary)

# If we output this string it will be the same as the string output by print()
print(mary_string)