################################################################################
#
# Program: Find The First Non-Repeating Item In A List
#
# Description: Find the first non-repeating item in a list using Python (i.e. 
# the first unique item in a list).
#
# YouTube Lesson: https://www.youtube.com/watch?v=S3ZjcPs37AU 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns the first non-repeating (unique) item in the list lst supplied as 
# an argument, or None if all items are repeating
def first_non_repeating(lst):
    
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
    # the value occurred only once in the list when counted above.
    for item in lst:
        if occurrences[item] == 1:
            return item 
    
    # If the loop above never returns all the items of the list (if it is not
    # empty) must be repeating and we can return None
    return None

# Create a test list and call function, we'll find 9 is the first non-repeating
# item in the list
numbers = [4,5,1,5,9,3,4,5,1,8,6,3,2,5,7,1,2,5]
print( first_non_repeating(numbers) )

# Create a test list and call the function, we'll find this list has no 
# non-repeating items and we get back None
other_numbers = [1,2,3,4,1,2,3,4]
print( first_non_repeating(other_numbers) )