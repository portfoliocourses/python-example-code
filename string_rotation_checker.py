################################################################################
#
# Program: Check If Strings Are Rotations Of Each Other
# 
# Description: Example of checking if a string is a rotation of another string
# using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=vYmftoG6JyQ 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns true if string1 and string2 are rotations of each other, and false 
# otherwise.
def is_rotation(string1, string2):
    
    # Strings of different lengths cannot be rotations, return false if so
    if len(string1) != len(string2):
        return False 
    
    # Otherwise we concatenate string1 with itself.  If string2 is a rotation
    # of string1, there will be an occurrence of string2 in string1.  If there 
    # is no occurrence of string2 in string1, then string2 is NOT a rotation 
    # of string1.  e.g. imagine we have string1 = "abcd" and string2 = "cdab"
    # where string1 is a rotation of string 2 (and vice versa), then 
    # concatenated string temp = "abcdabcd"
    #                               ----     <---- string2 occurs in temp!
    temp = string1 + string1 

    # Check if string2 is a substring of temp, i.e. does string2 occur in the 
    # concatenated string, and return true if so
    if string2 in temp:
        return True
    
    # Otherwise the strings are not rotations so we return false
    return False 

# Test strings which are rotations of each other
test1 = "python"
test2 = "thonpy"

# Output the return value of the function, which should be True in this case
print( is_rotation(test1, test2) )