################################################################################
#
# Program: Reverse A List Using Recursion
# 
# Description: Program to reverse a list using recursion in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=UiDzexaMY4Y
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The below function works using recursion by removing the last item in the 
# list, and concatenating a list containing only that item with the list 
# returned by calling the reverse function with the remaining portion of the
# list...
#
# return [lst.pop()] + reverse(lst)
#
# We call this the recursive step as the function calls itself.
#
# So if reverse is called with [5,6,7,8,9] the function will then return:
#
# [9] + reverse([5,6,7,8])
#
# And then the NEXT call to reverse will give us...
#
# [9] + [8] + reverse([5,6,7])
#
# And we can see how the list will be reversed one item at a time!  We stop
# the function from calling itself further when reverse is passed the 
# empty list with...
#
# if lst == []:
#     return []
#
# We call this the base case because this is when recursion stops.  So all
# together we will have:
#
# [9] + [8] + [7] + [6] + [5] + [] which results in the list [9,8,7,6,5].

# Returns a reversed version of the list lst using recursion
def reverse(lst):
    if lst == []:
        return []
    return [lst.pop()] + reverse(lst)

# Test list
numbers = [5,6,7,8,9]

# Output the reversed list returned by the reverse() function
print(reverse(numbers))