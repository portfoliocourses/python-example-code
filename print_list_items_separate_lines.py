################################################################################
#
# Program: Print List Items On Separate Lines
# 
# Description: Example of printing list items on separate lines using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=3ZdGucbtXgI 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A list of items
suits = ["Heart", "Club", "Diamond"]

# To output each item on a separate line we can put a * in front of the list
# variable name to pass each item individually to print, i.e. print will 
# be called like this: print("Heart", "Club", "Diamond")
#
# We can then use the keyword argument 'sep' to alter which character separates
# the arguments of print() when they are output, which by default is a space
# character.  We pass "\n" which is the newline character, so that after each
# item is output the newline character will be output so that each item 
# will output on a separate newline.

print(*suits, sep="\n")