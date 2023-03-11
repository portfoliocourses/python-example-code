################################################################################
#
# Program: Volume of a Sphere
# 
# Description: Compute the volume of a sphere using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=k6ZAUqT0_EU 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Import the math module so we can use its definition of pi with math.pi
import math

# Returns the volume of a sphere with radius r.  Note that r ** 3 will give us 
# the radius r to the power of 3.
def sphere_volume(r):
  return (4/3) * math.pi * (r ** 3)

# Prompt the user to enter in the radius using input(), the input() function 
# returns the string the user enters, which we convert to a float value with 
# float() before assigning the value to radius.
radius = float(input("Radius: "))

# Calculate the volume of the sphere using our function, passing the radius the
# user entered as an argument
volume = sphere_volume(radius)

# Output the calculated sphere volume
print("Sphere Volume: ")
print(volume)