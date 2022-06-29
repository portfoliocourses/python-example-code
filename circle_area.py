################################################################################
#
# Program: Circle Area
# 
# Description: Compute the area of a circle using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=48yLHoaTwvo 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Import the pi constant from the math library
from math import pi

# Define a function to compute the area of a circle, rounding the result to 
# 4 decimal digits of accuracy
def circ_area(r):
  return round(pi * r**2, 4)

# Prompt the user to enter a radius with input(), which returns a string, 
# convert that string to a float with float() and assign the result to radius
radius = float(input("Radius: "))

# Use the circle area function to compute the radius
area = circ_area(radius)

# Output the resulting area, we convert the area value to a string with str()
# concatenate it to "Area: " with +
print("Area: " + str(area))