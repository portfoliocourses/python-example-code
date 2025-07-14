################################################################################
#
# Program: Check If A String Is An Isogram
# 
# Description: Check if a sentence is a isogram using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=mYt3fmOxPl8
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Checks if  string s is an isogram and returns True if so and False otherwise
#
# A string is an isogram if it has no repeating letters from a-z (case 
# insensitive, i.e. an 'A' and 'a' in a string would be considered a repeating
# letter).  We don't consider non-letters characters like '-' or ' ' when 
# considering a string to be an isogram or not.
#
# This function works by first producing the string s with all letters made 
# lowercase using lower().  We then create a list made up of ONLY the letter 
# characters in the string using a list comphrension.  When we convert this 
# list to a set using set(), any duplicate letters will be removed as sets are
# not allowed to have duplicate items.  So if we compare the length of the list
# of letters to the length of the set of letters, they should be equal if the 
# string is an isogram because no duplicates will be removed, but if the string
# is not an isogram at least one duplicate will be removed and the lengths will
# not be the same.  The result of this comparison is used as the return value 
# of the function.
#
def is_isogram(s):
    low = s.lower()
    letters = [char for char in low if char.isalpha()]
    return len(letters) == len(set(letters))

# The firt two strings are isograms but the second is not so we should get back
# True, True and False as return values
print(is_isogram("Machine"))
print(is_isogram("Six-year-old"))
print(is_isogram("Alphabet"))