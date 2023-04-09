################################################################################
#
# Program: Repeat A String With The * Operator
# 
# Description: Examples of repeating a string using the * operator in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=GQFJJPJYATM 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# test string
string = "Python"

# string * 2 will create a new string made up of the original string repeated 2x
new_string = string * 2

# output the new string
print(new_string)

# string * 3 will create a new string made up of the original string repeated 3x
new_string = string * 3 

# output the new string
print(new_string)

# We could use the * operator in sitautions where we construct a string with a 
# repeated character or substring, e.g. creating a menu header for a console 
# application with repeated * characters.
menu = ("*" * 20) + " Menu " + ("*" * 20)

# Output the menu header string
print(menu)