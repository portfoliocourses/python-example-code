################################################################################
#
# Program: Rectangle Perimeter
# 
# Description: Compute the perimeter of a rectangle using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=Jxu8O1NOzpw 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns the perimeter of a rectangle rounded to 4 decimal places for a length 
# 'l' and a width 'w'
def rectangle_perimeter(l,w):
  return round(2 * (l + w), 4)

# Prompt the user to enter a length using input(), convert the string 
# returned by input() to a float using float() and assign the result to 
# length
length = float(input("Length: "))

# Do the same as the above for the rectangle's width
width = float(input("Width: "))

# Compute the perimeter of a rectangle using the function rectangle_perimeter()
perimeter = rectangle_perimeter(length,width)

# Output the computed perimeter of the rectangle, prepended with the text 
# "Perimeter:"
print("Perimeter:", perimeter)