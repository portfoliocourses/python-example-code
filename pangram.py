################################################################################
#
# Program: Check If A Sentence Is A Pangram
# 
# Description: Check if a sentence is a pangram using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=kypZMXGt3Zk
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

import string

# Returns True is the string s is a pangram and False otherwise.
#
# A pangram is a sentence containing the letters from a-z (case doesn't matter).
#
# We determine if the string is a pangram by making all letters lowercase (as 
# case does not matter).  We then turn the string into a set, which will give 
# us back a set with each letter of the string 's' as an item/string, e.g. 
# { 'T', 'h', ... }.  Because sets cannot contain duplicates, this will have 
# the effect of removing multiple occurrencs of characters, e.g. multiple o 
# characters in the sentence below.
#
# The ascii_lowercase constant is made up of the characters from a-z.  We 
# convert this to a set, and then use the issubset function to compare the 
# sets.  The function will return True if all the items in the set built 
# using ascii_lowercase (i.e. the letters from a-z) are found in the set 
# built using our sentence, thus checking if all the letters from a-z are 
# in the sentence.
#
def is_pangram(s):
    return set(string.ascii_lowercase).issubset( set(s.lower()) )

# Famous pangram example
print( is_pangram("The quick brown Fox jumps over the Lazy Dog") )

# Not a pangram
print( is_pangram("The quick brown jumps over the Lazy Dog") )
