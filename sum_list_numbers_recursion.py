################################################################################
#
# Program: Sum The Numbers In A List Using Recursion
#
# Description: Sum the numbers in a list using recursion with Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=KKxRNFFYaf0 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns the sum of the numbers in the list lst using recursion
#
# If the list is empty (not lst is True if the list lst is empty) we return 0
# as the sum of the numbers in an empty list is reasonably said to be 0.  This
# is also the "base case" where recursion will stop and function will stop 
# calling itself (also know as the "base step").
#
# Otherwise the function calls itself, returning the sum of the first item in
# the list as given by lst[0] with the sum of the remaining items in the list
# as given by calling sum_list with lst[1:] which uses the slicing operator 
# to obtain the remaining items in the list after the first item.  This is 
# called the "recursive case" or "recursive step", as the function calls itself,
# solving part of the problem and calling itself with a smaller version of the 
# same problem as is often the case with recursive solutions to problems.
#
# Eventually the function will stop calling itself when the remaining portion
# of the list is empty.
#
def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:]) 
   

# Test the function with a list of numbers.  Recursion will look like this in
# this case...
#
# sum_list([4,1,3])
#   |
#   4 + sum_list([1,3])
#         |
#         1 + sum_list([3])
#               |
#               3 + sum_list([])
#                     |
#                     0
#
numbers = [4,1,3]
print( sum_list(numbers) )

# Test the function with the empty list
numbers = []
print( sum_list(numbers) )