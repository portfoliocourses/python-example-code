################################################################################
#
# Program: __mul__ and __rmul__ Method Examples
# 
# Description: Example of using the __mul__ and __rmul__ magic methods (i.e. 
# dunder methods) in Python to define how the addition operator (*) should 
# behave for a type of object (i.e. operator overloading).
#
# YouTube Lesson: https://www.youtube.com/watch?v=wYw9r3JIkY8 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A simple class to represent a population
class Population:

    # When population objects are initialized they will have a count attribute
    # initialized to some initial count
    def __init__(self, initial_count):
        self.count = initial_count 

    # This function is called when we have either:
    #
    # PopulationObject * PopulationObject
    #
    # OR 
    #
    # PopulationObject * NumberObject
    #
    # Where NumberObject is some type of number in Python.  The function 
    # supports both cases of the right operand being either a Population-type
    # object or some kind of number type object in Python.  
    #
    # We define how the multiplication operator should behave in this case 
    # by returning a new Population object.  In the case of multiplying 
    # two Population objects we set the new Population object's count to 
    # the product of the two Population object's counts.  In the case of 
    # multiplying a Population object by a number, we set the new Population
    # object's count to the product of the Population operand object's count 
    # and the number.
    #
    # The isinstance() function will return True if other is a type of number
    # in Python.
    #
    def __mul__(self, other):
        if (isinstance(other, Number)):
            return Population(self.count * other)
        return Population(self.count * other.count)
    
    # In the case that we have...
    #
    # NumberObject * PopulationObject
    #
    # Then the __mul__ method of the number type object will not know how to
    # work with a Population type object, and the below __rmul__ method will
    # be called instead with self set to the right PopulationObject and other 
    # set to NumberObject.  Because we want * to be commutative 
    # (i.e. a * b == b * a) we can return the result of calling the __mul__ 
    # method with other/NumberObject as an argument.
    #
    # Note that in general when we have left_operand * right_operand the 
    # __rmul__ method of right_operand will be called when either:
    #
    # 1) the __mul__ method is not defined for left_operand
    # 2) the __mul__ method returns NotImplemented
    #    
    def __rmul__(self, other):
       return self.__mul__(other)

# Create two Population objects
population1 = Population(100)
population2 = Population(5)

# This would result in a call to __mul__ and a new Population object with a 
# count of 500...
#
# new_population = population1 * population2

# This would result in a call to __mul__ and a new Population object with a
# count of 500, but this time 'other' will be an instance of type Number 
# because 5 is an int value (which is a type of Number in Python).
#
# new_population = population1 * 5

# This would result in a call to __rmul__ because the Float object 5.5. does
# not have a __mul__ method that supports working with a Population object
# as a right operand.
#
new_population = 5.5 * population1 

# Output the count of the new Population object...
print(new_population.count) 
