################################################################################
#
# Program: String endswith() Method
# 
# Description: Examples of using the string endswith() method in Python to 
# check if a string ends with another string.
#
# YouTube Lesson: https://www.youtube.com/watch?v=D4VlfokXYDo 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Create a test string.  Note that each character in the string has an index 
# from 0 ... 9 as below.
#
#         0123456789
string = "Carol Shaw"

# The endswith() method will return true if the string ends with the string that
# is provided as an argument.  In this case our test string does end with "Shaw"
# so the method will return true.
print( string.endswith("Shaw") )

# The test string does not end with Carol so endswith() will return false.
print( string.endswith("Carol") )

# The string technically does end "with itself" so endswith() will return true
# in this case...
print( string.endswith("Carol Shaw") )

# We can optionally supply a start index as an argument, and the search will 
# begin at this start index.  So this will check the test string from the index
# 4 onwards to see if it ends with "Shaw", which it does, and so endswith() 
# will return true.
print( string.endswith("Shaw", 4) )

# If our start index is 7, then our test string is "haw" from the index 7 
# onwards, and therefore the string from the start index onwards does NOT end 
# with "Shaw" and endswith() will return false.
print( string.endswith("Shaw", 7) )

# We can also optionally supply an end index, and the search will take place 
# from the start index up to but not including the end index.  So the below 
# call to the method will check if the test string from indexes 6...9 ends with
# "Shaw", which it does, and endswith() will return true.
print( string.endswith("Shaw", 6, 10) )

# This method call will check if the string from the indexes 6 ... 7 ends with
# "h", which it does, and endswith() will return true.
print( string.endswith("h", 6, 8) )

# We can also supply a tuple as a first argument instead of a string, and 
# endswith() will return true if the string ends with any of the strings in 
# the tuple.  In this case "Shaw" is in the tuple and the string does end with
# "Shaw" and so endswith() will return true.
print( string.endswith( ("Shaw", "Smith") ) )