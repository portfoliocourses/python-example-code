################################################################################
#
# Program: Find The First Repeating Item In A List
#
# Description: Find the first repeating item in a list using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=fHLDc8t1x4c 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns the first repeating item in the list lst supplied as an argument, or 
# None if no items are repeating
def first_repeating(lst):
 
    # Dictionary to keep track of number of occurrences of each value in list
    occurrences = {}

    # Loop through each item in the list and count the occurrences of each 
    # value that occurs.  If we encounter a value for the first time, we set
    # a key for that value in the dictionary to 1 as we have encountered the
    # value 1 time.  If we have already encountered the value before, it will
    # be in the occurrences dictionary, and we can increment the existing 
    # count by 1.
    for item in lst:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1

    # Loop through the items in list again, and return the first item where 
    # the value occurred more than once in the list when counted above.
    for item in lst:
        if occurrences[item] > 1:
            return item 

    # If the loop above never returns all the items of the list (if it is not
    # empty) must be unique and we can return None
    return None

# Create a test list and call the function and we'll find 4 is the first 
# repeating item in the list
numbers = [1,2,3,4,5,6,7,8,9,4,5,6,7,8,4,5,6]
print( first_repeating(numbers) )

# Create a test list and call the function, we'll find this list has no 
# repeating items and we get back None
other_numbers = [1,2,3,4,5,6,7,8]
print( first_repeating(other_numbers) )