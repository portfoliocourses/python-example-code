################################################################################
#
# Program: Count The Occurrences Of Each Item In A List
#
# Description: Count the occurrences of each item (value) in a list with Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=TOkSElso_Fk 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# We can use the built-in Counter class of the collections module to solve this
# problem (or we could create our own function like find_counts())
from collections import Counter

# Returns a dictionary containing the number of occurrences of each value/item
# in the lst list, where the dictionary keys are the values/items that occur in
# the list and they are set to the number of occurrences of those values/items.
def find_counts(lst):
    
    # Begin with an empty dictionary as we have counted no occurrences of any
    # values yet
    counts = {}
    
    # Loop through each item in the list, if it's the first time we've 
    # encountered the value it won't be in the dictionary so create a new
    # key for the value (item) and set it to 1, otherwise if the value 
    # already is in the dictionary we increment the running count of the 
    # number of occurrences of the value.
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    
    # return the dictionary
    return counts


# A test list of numbers
numbers = [1,4,5,8,3,5,6,8,9,1,3,5,6,8,5,7,8]

# The Counter() object produced when passed numbers will contain a count of the
# number of occurrences of each value in the list.
counts = Counter(numbers)

# We can see this if we output counts
print(counts) 

# We can access the Counter() object much like a dictionary, e.g. the below 
# will give us the number of occurrences of the value 7 in our numbers list
print(counts[7]) 

# We can loop through the keys of the Counter object like we would a dictionary
# and output the count of the number of occurrences of each value in the list
for item in counts:
    print(item, "-", counts[item])

# Test out the find_counts() function
counts_again = find_counts(numbers)

# If like above we loop through the keys of the dictionary we can output the 
# count of the number of occurrences of each value in the list and we'll find it
# matches what the Counter() object contains!
for item in counts_again:
    print(item, "-", counts[item])
