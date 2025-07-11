################################################################################
#
# Program: Check If All List Items Are Unique
# 
# Description: Check if all list items are unique in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=uAQST2Psgn4
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A list with a duplicate item - 5
my_list = [1,2,3,5,4,5]   

# When we convert a list to a set with set() any duplicate items will be removed
# because set items MUST be unique.  We can then check the length of the set and
# origina list using len(), if the list ONLY contained unique items then no items
# should be removed when it is converted to a set and the lengths should be the 
# same.  Otherwise the list must have contained at least one duplicate item, in
# which case we report that not all item in the list are unique.
#
if len(set(my_list)) == len(my_list):
    print("All items in the list are unique")
else:
    print("Not all items in the list are unique")