################################################################################
#
# Program: any() Built-In Function Examples
#
# Description: Examples of using the built-in any() function in Python to check
# if any item in an iterable object is true.
#
# YouTube Lesson: https://www.youtube.com/watch?v=S_fEefXslrI 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The built-in any() function will return True if any item in the iterable 
# object it is passed an argument is true.  In the below list the last item is
# True so the any() function will return True (which we output with print()).
print(any([False, False, True]))

# any() function will return False as all items are false
print(any([False, False, False ]))

# The any() function will work with items that evaluate to True or False, 
# such as "abc" which evaluates to True and so the any() function returns True
print(any([False, False, "abc"]))

# "" evaluates to False so any() returns False
print(any([False, False, ""]))

# any() returns False for an empty iterable such as the empty list
print(any([]))

# any() works with iterable objects of different types such as sets, where 
# below 0 evaluates to False and 1 evaluates to True so any() returns True
print(any({0, 1}))

# any() returns False with the set containing only 0 which evaluates to False
print(any({0}))

# When passed a dictionary any() checks the KEYS of the dictionary and returns
# True if any are True, so with a key of 0 which evaluates to False and a key
# of 1 which evaluates to True any() returns True below.
print(any({0: True, 1: True}))

# When the dictionary only has a key 0 which evaluates to False it returns False
print(any({0: True}))

# One good use case of any() comes from using it with list comprehensions. Say
# we have a list of strings and we wish to check if any of the strings start 
# with "aga". We could use a loop structure to go through and check if any item 
# starts with "aga", or we could use a single line of code using any() and 
# a list comprehension instead.
strings = ["apple", "against", "application"]

# The list comprehension uses the startswith() method with each string in the 
# above list to produce a list of True/False values depending on whether each
# string starts with "aga".  We then use any() to verify if ANY of the strings
# start with "aga" (which will be the case if any of the list items are True in
# the list produced by the list comprehension).
if any([s.startswith("aga") for s in strings]):
    print("a string does begin with 'aga'")
else:
    print("no string begins with 'aga'")