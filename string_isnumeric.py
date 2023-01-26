################################################################################
#
# Program: String isnumeric() Method
# 
# Description: Examples of using the isnumeric() method in Python to check if 
# all of the characters in a string are numeric.
#
# YouTube Lesson: https://www.youtube.com/watch?v=ufE3wUTKDLU 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# isnumeric() will return true if all the characters in the string are numeric,
# and false otherwise

# The digits from 0-9 are numeric, so the method returns true for this string
string = "0123456789"  
print( string.isnumeric() )

# A space character is not numeric, so the method returns false for this string
string = "012345 6789"  
print( string.isnumeric() )

# A punctuation mark like period . is not numeric, so the method returns false
string = "012345.6789"  
print( string.isnumeric() )

# There are characters aside from the digits 0-9 that are numeric, so the 
# superscript digits, roman numerals, and fractional characters are also 
# considered to be numeric.
string = "0123456789²Ⅻ½"  
print( string.isnumeric() )