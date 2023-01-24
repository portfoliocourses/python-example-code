################################################################################
#
# Program: String isalnum() Method
# 
# Description: Examples of using the isalnum() method in Python to check if all
# of the characters in a string are alphanumeric (i.e. either letters or 
# numeric).
#
# YouTube Lesson: https://www.youtube.com/watch?v=RNXDpPy1pcA 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# isalnum() returns true if the string contains only alphanumeric characters and
# false otherwise, we test it out below...

# Letters a-z, A-Z and digits 0-9 are considered alphanumeric so isalnum() will
# return true.
string = "ABCabc123"
print( string.isalnum() )

# Whitespace 'space' character is NOT considered alphanumeric so isalnum() will
# return false.
string = "ABCabc 123"
print( string.isalnum() )

# Punctuation 'period' character is NOT considered alphanumeric so isalnum() 
# will return false.
string = "ABCabc.123"
print( string.isalnum() )

# Letters from international alphabets such as ß are considered alphabetic and 
# characters such as 'superscript 2' and roman numerals are considered numeric,
# so isalnum() will return true.
string = "ABCabc123ß²Ⅻ"
print( string.isalnum() )