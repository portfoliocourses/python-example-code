################################################################################
#
# Program: Area of a Rectangle
# 
# Description: Compute the area of a rectangle using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=XLyDZ6RQYGI 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns the area of a rectangle rounded to 4 decimal places for a length 'l'
# and a width 'w'
def rectangle_area(l,w):
  return round(l * w, 4)

# Prompt the user to enter a length using input(), convert the string 
# returned by input() to a float using float() and assign the result to 
# length
length = float(input("Length: "))

# Do the same as the above for the rectangle's width
width = float(input("Width: "))

# Compute the area of a rectangle using the function rectangle_area()
area = rectangle_area(length,width)

# Output the computed area of the rectangle, prepended with the text "Area:"
print("Area:", area)