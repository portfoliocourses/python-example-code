################################################################################
#
# Program: Reverse A String
# 
# Description: Example of reversing a string in Python using string slicing.
#
# YouTube Lesson: https://www.youtube.com/watch?v=M5iVFGU3VoI
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Each character in a string is stored at an index, starting from 0...
#
#         0123456789
string = "try it out"

# We can use string slicing to create a new string from the characters of an 
# existing string.  Here we supply a start value of 0, a stop value of 6, and
# a step value of 2.  This will create a new string from the characters in the 
# original string, pulling the characters from the index 0 up until but not 
# including index 6, stepping by 2... i.e. the string "tyi".
#
#           X X X ----
#           0123456789
# string = "try it out"
#
new_string = string[0:6:2]

print(new_string) 


# We can also have a negative step value, which will pull the characters "in 
# reverse", i.e. here we will pull the characters from the index 9 up until but
# not including index 6 in reverse stepping by 1, resulting in the string "tuo".
#
#           *******<--
#           0123456789
# string = "try it out"
#
new_string = string[9:6:-1]

print(new_string) 


# If we leave out the start and stop values, when the step value is negative the
# characters will be pulled from the very end of the string to the very start of
# the string.  So with a step value of -1, we pull each character one at a time
# in reverse from the very end of the string to the very start, i.e. we get back
# the reversed string!
new_string = string[::-1]

print(new_string) 