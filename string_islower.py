################################################################################
#
# Program: String islower() Method
# 
# Description: Examples of using the islower() method in Python to check if all
# of the letters in a string are lowercase.
#
# YouTube Lesson: https://www.youtube.com/watch?v=lFnuT7H-6nE  
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# This string contains 2 uppercase letters, and so we expect islower() to return
# false.
string = "A string, with 2 Uppercase letters"
print( string.islower() )

# All letters in the string are lowercase, so we expect the method to return 
# true. The method will ignore non-letter characters such as spaces, digits and
# punctuation marks. 
string = "a string, with 2 uppercase letters"
print( string.islower() )