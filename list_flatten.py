################################################################################
#
# Program: Flatten A List
# 
# Description: Flatten a list of lists using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=9GKWwMbCRKw
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A list of lists
nested = [ [1,2,3], [4,5], [7,8,9] ]

# The list comprehension produces a new list by essentially looping over each
# sublist with 'for sublist in nested' and for each sublist looping over each
# item with 'for item in sublist'.  The 'item' at the start of the list 
# comprehension effectively places each of these items in the new list that is 
# created.
flat = [item for sublist in nested for item in sublist]

# Output the flattened list
print(flat)