################################################################################
#
# Program: Check If All String Characters Are Unique
# 
# Description: Check if all the characters in a string are unique using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=HEhdM7zdy68 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns true if all characters in the string are unique and false otherwise
def check_unique(string):
    
    # Keeps track of the unique characters found in the string "so far"
    unique_characters = []
    
    # Loop through the string one character at a time and check to see if the
    # character was previously encountered (i.e. is the character NOT unique)
    # by checking to see if it's already in the unique_characters list.  If it 
    # IS already in the unique characters list, we can return False as we have
    # established not all characters in the string are unique.  Otherwise this
    # character is a NEW unique character so we append it to the 
    # unique_characters list.
    #
    for character in string:
        if character in unique_characters:
            return False
        else:
            unique_characters.append(character)

    # If we go through all characters in the string and all of them are unique
    # we can return True
    return True

# Test out the function
test = "abcd"
print( check_unique(test) )