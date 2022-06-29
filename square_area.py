################################################################################
#
# Program: Area of a Square
# 
# Description: Compute the area of a square using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=rS8xCIQiWJo 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns the area of a square rounded to 4 decimal places for a given side 
# length 'l'
def square_area(l):
  return round(l ** 2, 4)

# Prompt the user to enter a side length using input(), convert the string 
# returned by input() to a float using float() and assign the result to 
# side_length
side_length = float(input("Side Length: "))

# Compute the area of a square using the function square_area()
area = square_area(side_length)

# Output the square area, use str() to convert the area numeric value to a 
# string and concatenate that string to "Area: " with +
print("Area: " + str(area))