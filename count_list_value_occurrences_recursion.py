################################################################################
#
# Program: Count The Occurrences Of A Value In A List Using Recursion
#
# Description: Count the occurrences of a value in a list using recursion in
# Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=LmSKX5vTWAU 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns the occurrences of the parameter value in the list parameter lst.
#
# If the list is empty (not lst is True if the list lst is empty) we return 0
# as the value cannot occur any times in a list that is empty.  This
# is also the "base case" where recursion will stop and function will stop 
# calling itself (also know as the "base step").
#
# Otherwise if the first item in the list matches the value we are looking for 
# we return 1 plus the number of occurrences of the value in the remaining 
# portion of the list.  We use the count function to obtain the number of 
# occurrences in the remaining portion of the list, passing it lst[1:] which 
# uses the slicing operator to give us the list containing all the items 
# after the first item.  If we first item in the list does not match the value
# we are looking for then we just return the number of occurrences of the value
# in the remaining portion of the list.
#
# Eventually the function will stop calling itself when the remaining portion
# of the list is empty.
#

def count(lst, value):
    if not lst:
        return 0
    elif lst[0] == value:
        return 1 + count(lst[1:], value)
    else:
        return count(lst[1:], value)


# Test the function with a list of numbers, count the occurrences of 4 (2).
#
numbers = [4,1,4,2]
print( count(numbers, 4) )