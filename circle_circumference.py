################################################################################
#
# Program: Circle Circumference
# 
# Description: Compute the circumference of a circle using Python 
# (i.e. the perimeter of a circle).
#
# YouTube Lesson: https://www.youtube.com/watch?v=y3sXDqMDA2k 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Import the pi constant from the math library
from math import pi

# Define a function to compute the circumference of a circle, rounding the 
# result to 2 decimal digits of accuracy
def circ_circumference(r):
  return round(2 * pi * r, 2)

# Prompt the user to enter a radius with input(), which returns a string, 
# convert that string to a float with float() and assign the result to radius
radius = float(input("Radius: "))

# Use the circle circumference function to compute the radius
circumference = circ_circumference(radius)

# Output the resulting circumference, we convert the circumference value to a 
# string with str() concatenate it to "Circumference: " with +
print("Circumference: " + str(circumference))