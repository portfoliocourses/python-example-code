################################################################################
#
# Program: Remove Duplicate Items From A List
# 
# Description: Approaches to remove duplicate items from a list in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=YH6jEuV_0fg
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Sample list with duplicates
my_list = [1,1,1,2,2,3,3,3,3]

# We can convert the list to a set using set(), sets do not have duplicates and
# so duplicate items will be removed when we do so.  We then convert the set 
# back to a list to get the list with duplicates removed.  The only issue with 
# this approach is that the order of the items may not be perserved.
#
# unique_list = list(set(my_list))

# As of Python 3.7 we can use the fromkeys method of the dictionary data 
# structure to create a dictionary with keys made up of the unique items of 
# our list AND the order will be preserved.  We can use list() to produce a list
# using this dictionary, where the keys of the dictionary will become the items
# of the unique list.
# 
# unique_list = list(dict.fromkeys(my_list))

# We could manually build a list made up of the unique items of the original 
# list by looping through each item of the original list and only appending it 
# to the new list if it is not already in the new list.  In this way, only 
# unique items will be transfered over to the new list.
#
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
 
# Output the resulting list with only the unique items of the original list
print(unique_list)