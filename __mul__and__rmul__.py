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

class Population:

    def __init__(self, initial_count):
        self.count = initial_count 

    def __mul__(self, other):
        if (isinstance(other, Number)):
            return Population(self.count * other)
        return Population(self.count * other.count)
    
    def __rmul__(self, other):
       return self.__mul__(other)

population1 = Population(100)
  
new_population = 5.5 * population1 
print(new_population.count) 