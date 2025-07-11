################################################################################
#
# Program: Loop Over A List In Reverse
# 
# Description: Loop over the items in a list in reverse using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=RCnA3BKzrgo
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Test list
fruits = ["apple", "banana", "pear"]

# Loops over the items in the list in reverse.  The reversed() function that is
# built-in to Python does not reverse the list or produce a new list, what it 
# does is return an iterator that allows us to iterate over the items in the 
# list in reverse.  The for loop uses the iterator to iterate over the list 
# items in reverse.
#
for fruit in reversed(fruits):
    print(fruit)