################################################################################
#
# Program: all() Built-In Function Examples
#
# Description: Examples of using the built-in all() function in Python to check
# if all the values in an iterable object are true.
#
# YouTube Lesson: https://www.youtube.com/watch?v=E2j4QjDyXzs 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The all() function built-in to Python returns True if all the items of an 
# iterable object such as a list or set are true, so the below call to all()
# will return True...
print(all( [True, True, True] ))

# With a False item in the iterable all() will return False
print(all( [True, True, False] ))

# all() will work with items that evaluate to True or False, so because "abc"
# evaluates to True all() will return True
print(all( [True, True, "abc"] ))

# "" evaluates to False so all() will return False
print(all( [True, True, ""] ))

# all() will return True for empty iterable objects such as the empty list
print(all( [] ))

# all() will work with iterables of all types such as a set containing 1,2,3
# which all evaluate to True (so all() will return True)
print(all( {1,2,3} ))

# 0 evaluates to False so all() will return False
print(all( {1,2,0} ))

# In the case of a dictionary iterable object all() will check if the keys
# are all true, so with keys 1 and 2 being true all() returns True below
print(all( {1: False, 2: False} ))

# But with the key 0 being false all() will return False below
print(all( {1: False, 0: False} ))

# One good use case of all() comes from using it with list comprehensions. Say
# we have a list of strings and we wish to check if all the strings start with
# "appl". We could use a loop structure to go through and check if each item 
# starts with "appl", or we could use a single line of code using all() and 
# a list comprehension instead.
strings = ["apple", "against", "application"]

# The list comprehension uses the startswith() method with each string in the 
# above list to produce a list of True/False values depending on whether each
# string starts with "appl".  We then use all() to verify if ALL the strings
# start with "appl" (which will be the case if all list items are True in the
# list produced by the list comprehension).
if all( [s.startswith("appl") for s in strings] ):
    print("all the items begin with 'appl'")
else:
    print("all the items do not begin with 'appl'")