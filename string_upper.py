################################################################################
#
# Program: String upper() Method
# 
# Description: Examples of using the upper() method in Python to make all of the
# letters in a string uppercase.
#
# YouTube Lesson: https://www.youtube.com/watch?v=yAba1XZ6PNA 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Create a test string
string = "Some OF the LETTERS Are LowerCase"

# The .upper() method will return a new string identical to the original string
# except all lowercase letters will be turned into uppercase letters.  The 
# method will ignore all other characters (numbers, digits, etc.).
new_string = string.upper()

# Output the new string to confirm all letters have been made uppercase
print(new_string)