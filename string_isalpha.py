################################################################################
#
# Program: String isalpha() Method
# 
# Description: Examples of using the isalpha() method in Python to check if all
# of the characters in a string are letters.
#
# YouTube Lesson: https://www.youtube.com/watch?v=TWlRjAqxVH8 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# All of the characters in this string are letters (either uppercase or 
# lowercase), so the method will return true.
string = "abcDEF"
print( string.isalpha() )

# Even one non-alphabetical character in a string will cause the method to
# return false, so this space character at the end of the string will cause the
# method to return false.
string = "abcDEF "
print( string.isalpha() )

# Any non-alphabetical character will cause the method to return false, for 
# example in this case a digit, though other characters such as whitespace, 
# punctuation, etc will all cause the method to return false.
string = "abc2DEF"
print( string.isalpha() )

# The method does recognize characters from "international alphabets" as 
# alphabetical characters, so for example this German word below will cause 
# the method to return true.
string = "heißt"
print( string.isalpha() )