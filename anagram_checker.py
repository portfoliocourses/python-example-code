################################################################################
#
# Program: Check If Two Strings Are Anagrams
# 
# Description: Check if two strings are anagrams using Python, where two strings
# are considered anagrams if they contain the same letters: 
#   https://en.wikipedia.org/wiki/Anagram
#
# YouTube Lesson: https://www.youtube.com/watch?v=Zpsw6YCHyDs 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns True if s1 and s2 are anagrams, and False otherwise
def check_anagram(s1,s2):
    s1_list = sorted(s1.lower().replace(" ", ""))
    s2_list = sorted(s2.lower().replace(" ", ""))
    return s1_list == s2_list

# Two strings that are anagrams
string1 = "Tom Marvolo Riddle"
string2 = "I am Lord Voldemort"

# The sorted() function returns an alphabetically sorted list of the characters
# in a string.  The above function works by first removing all space characters 
# in the strings using replace(), and setting all characters to lowercase using
# lower().  This ensures that space characters and the capitalization of the 
# letters do not affect whether strings are considered anagrams or not.  We then
# use sorted() on both strings, and if the two strings are anagrams containing 
# the same letters, then the two lists should be identical.  So we check the 
# lists for equality using == as the check to see if the two strings are
# anagrams or not.
#
print( sorted(string1) )
print( sorted(string2) )

# Check if the two strings are anagrams and output the result
print( check_anagram(string1, string2) )