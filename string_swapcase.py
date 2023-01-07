################################################################################
#
# Program: String swapcase() Method
# 
# Description: An example of using the string swapcase() method in Python. 
#
# YouTube Lesson: https://www.youtube.com/watch?v=5J5PqC4_0v4 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Create a string with a couple uppercase letters (P,C) and the rest lowercase
string = "Portfolio Courses"

# swapcase will return a new string that is the same as the original string
# except lowercase letters will be replaced/swapped with their uppercase 
# versions and uppercase letters will be replaced/swapped with their lowercase
# versions.
new_string = string.swapcase()

# Ouput the new string to verify the letters have been swapped
print(new_string)

# Note that swapcase does not modify the existing string, i.e. string will 
# remain unchanged
print(string)