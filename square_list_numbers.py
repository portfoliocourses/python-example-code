################################################################################
#
# Program: Square The Numbers In A List
# 
# Description: Square the numbers in a list using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=uUI3Z9da4Us 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Test list
list = [1,2,3,4,5]

# A list comprehension can be used to square the numbers in the list.  This list
# comprehension will produce a new list by squaring each number in the list
# above.
squared = [num * num for num in list]

# We could also solve this problem in a more "manual" way by creating an empty
# list, looping through each number in the list and appending the square of
# the number to the new list.
#
# squared = []
#
# for number in list:
#   squared.append(number * number)

# Output the squared list
print(squared)