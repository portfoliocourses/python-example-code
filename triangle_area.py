################################################################################
#
# Program: Area of a Triangle
# 
# Description: Compute the area of a triangle using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=EV-XX-__Pss 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns the area of a triangle rounded to 4 decimal places for a base 'b' and
# a height 'h'
def triangle_area(b,h):
  return round(0.5 * b * h, 4)

# Prompt the user to enter a base using input(), convert the string 
# returned by input() to a float using float() and assign the result to 
# base
base = float(input("Base: "))

# Do the same as the above for the triangle's height
height = float(input("Height: "))

# Compute the area of the triangle using the function triangle_area()
area = triangle_area(base,height)

# Output the computed area of the triangle, prepended with the text "Area:"
print("Area:", area)