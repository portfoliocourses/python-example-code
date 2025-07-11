################################################################################
#
# Program: Remove Empty Strings From A List
# 
# Description: Remove the empty strings from a list using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=QLYaiFdHbhU
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A list with a couple empty strings
strings = ["portfolio", "", "courses", "", "subscribe"]

# The list comprehension [ ... ] produces a new list by checking every string 
# 's' in strings, and "if s" is true then the string 's' is put into the new 
# list.  "if s" evalutes to False if the string is empty and True if the string
# is non-empty in Python, so only the non-empty strings will be in the new list!
#
new_strings = [s for s in strings if s]

# Output the new list
print(new_strings)