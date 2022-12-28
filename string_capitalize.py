################################################################################
#
# Program: String capitalize() Method
# 
# Description: An example of using the string capitalize() method in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=bkcw3KCoXFo 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# An example string
string = "portfolio COURSES"

# The string .capitalize() method will return a new string.  If the old string 
# has a lowercase letter as its first character, that letter will be turned 
# into an uppercase letter in the new string.  Any remaining letters in the 
# string will be turned into lowercase letters.
new_string = string.capitalize()

# Output the new string
print(new_string)

# Note that calling capitalize will not modify the old string
print(string)