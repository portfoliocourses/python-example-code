################################################################################
#
# Program: Replace A Range Of List Items
# 
# Description: Examples of replacing a range of list items in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=9jTj4eN42GI 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Example list of letters, with each string at an index...
#
# Index:    0    1    2    3
letters = ["A", "B", "C", "D"]

# Replace the range of items from the index 1 up until but not including the 
# index 3 (i.e. "B" and "C") with the new items "X" and "Y"
letters[1:3] = ["X", "Y"]

# Output the list to verify the replacement occurred
print(letters)


# Reset the example list to its original state
letters = ["A", "B", "C", "D"]

# If there are more items in the list of replacement items than there are items
# in the list to be replaced, than the remaining items in the list (in this case
# "D") will be shifted down
letters[1:3] = ["X", "Y", "Z"]

# Output the resulting list 
print(letters)


# Reset the example list to its original state
letters = ["A", "B", "C", "D"]

# If there are fewer items in the list of replacement items than there are items
# in the list to be replaced, than the remaining items in the list (in this case
# "D") will be shifted forward
letters[1:3] = ["X"]

# Output the resulting list 
print(letters)


# Reset the example list to its original state
letters = ["A", "B", "C", "D"]

# We can also use a step value when specifying the range, so that when each item
# is selected from the start to the stop index, we skip ahead step number of 
# indexes to select the next item.  So in this case "A" and "C" will be selected
# at the indexes 0 and 2, and "A" will be replaced with "X" and "C" will be 
# replaced with "Y".
letters[0:4:2] = ["X", "Y"] 
 
# Output the resulting list
print(letters)