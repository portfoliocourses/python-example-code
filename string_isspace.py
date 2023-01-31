################################################################################
#
# Program: String isspace() Method
# 
# Description: An example of using the string isspace() method in Python to 
# check if all of the characters in a string are whitespace characters. 
#
# YouTube Lesson: https://www.youtube.com/watch?v=gC-iPeWasrY 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The isspace() string method will return true if all the characters in a 
# string are whitespace characters, and false otherwise.

# The ' ' space character, \n newline and \t tab are the most common whitespace
# characters.  Because the below string contains ONLY whitespace characters the
# isspace() method will return true.
string = " \n\t"
print( string.isspace() )

# There are other whitespace characters such as \v vertical tab, \r carriage 
# return, and \f form feed.  Again beause the string is ONLY made up of 
# whitespace characters, the isspace() method will return true.
string = " \n\t\v\r\f"
print( string.isspace() )

# If the string contains even one non-whitespace character such as the letter 
# lowercase a then the method will return false as below.
string = " a \n\t\v\r\f"
print( string.isspace() )