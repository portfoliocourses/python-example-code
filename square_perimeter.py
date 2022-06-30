################################################################################
#
# Program: Perimeter of a Square
# 
# Description: Compute the perimeter of a square using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=T_h7SR4U57Y 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns the perimeter of a square rounded to 2 decimal places for a given side 
# length 'l'
def square_perimeter(l):
  return round(l * 4, 2)

# Prompt the user to enter a side length using input(), convert the string 
# returned by input() to a float using float() and assign the result to 
# side_length
side_length = float(input("Side Length: "))

# Compute the perimeter of a square using the function square_perimeter()
perimeter = square_perimeter(side_length)

# Output the square perimeter, use str() to convert the perimeter numeric value 
# to a string and concatenate that string to "Perimeter: " with +
print("Perimeter: " + str(perimeter))