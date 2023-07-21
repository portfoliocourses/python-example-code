################################################################################
#
# Program: Convert Miles To Kilometers
# 
# Description: Convert miles to kilometers using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=StFx57DxND8 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Prompt the user to enter the distance in miles using input(), the 
# function will return the text entered by the user as a string, convert that 
# string to a float value with float() and store it into miles (so that we 
# can perform mathematical operations with the value).
miles = float(input("Miles: "))

# Convert the distance to kilometers and store it into the variable miles using
# the formula: https://en.wikipedia.org/wiki/Kilometre
kilometers = miles / 0.621371

# Output the text "Kilometers:" followed by the value in the variable kilometers
print("Kilometers:", kilometers)
 
# Alternatively, we could use an f-string to output the kilometers with 
# 2 decimal digits of precision with .2 and in fixed-point notation with .2f
print(f"Kilometers: {kilometers:.2f}")