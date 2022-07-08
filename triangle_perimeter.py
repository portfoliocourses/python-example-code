################################################################################
#
# Program: Perimeter of a Triangle
# 
# Description: Compute the perimeter of a triangle using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=svFm8KtbDMs 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns the perimeter of a triangle rounded to 4 decimal places with side 
# lengths a, b, and c
def triangle_perimeter(a,b,c):
  return round(a + b + c, 4)

# Prompt the user to enter a side length 'a' using input(), convert the string 
# returned by input() to a float using float() and assign the result to side_a
side_a = float(input("Side A: "))

# Do the same for side lengths 'b' and 'c'
side_b = float(input("Side B: "))
side_c = float(input("Side C: "))

# Compute the perimeter of the triangle using the function triangle_perimeter()
perimeter = triangle_perimeter(side_a,side_b,side_c)

# Output the computed perimeter of the triangle, prepended with "Perimeter:"
print("Perimeter:", perimeter)