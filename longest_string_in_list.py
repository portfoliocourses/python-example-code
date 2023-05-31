################################################################################
#
# Program: Find The Longest String In A List
#
# Description: Program to find the longest string in a list using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=d_z9dmIUcvQ 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# There are many ways we could find the longest string in a list using Python.
# We could implement our own algorithm using a loop and if-statement, or we 
# could solve the problem in one line using the built-in max() function.  Both
# solutions are presented below.

# A list of strings where Orange is the longest string in the list
strings = ["Red", "Orange", "Green"] 

# Solution #1: Algorithm Implementation

# The below algorithm will find the longest string in the list by checking each
# string in the list one after the other from the first string in the list to 
# the last string in the last.  Every time a string is found which has a length
# longer than the longest string found so far, we update "longest string 
# found so far" variables that keep track of the length of the longest string 
# found so far and the string itself.  We initially set the variable 
# (max_length) keeping track of the length of the longest string found so far 
# to -1 as ANY string in the list will be longer than this, including the first
# string.  We initially set the variable (max_string) keeping track of the 
# longest string found so far to None as initially no such string exists.  We 
# use the len() function to find the length of each string.  We use a for loop 
# to loop through each string in the list, and an if-statement to check if 
# the current string being examined is longer than the longest string found 
# so far, and if it is we update max_length and max_string accordingly.  By 
# the end of the for loop's execution max_string will be set to the longest 
# string in the list.

max_length = -1
max_string = None
for string in strings:
    if len(string) > max_length:
        max_length = len(string)
        max_string = string

# Output the longest string in the list
print(max_string)


# Solution #2: Built-In max() Function Call

# The max() function is built-in to Python and will return the lexicographically
# largest string if passed the list.  But if we use the optional parameter 'key'
# and pass the function len() as an argument, the len() function will be applied
# to each item in the list, and the return value of those function calls (the 
# string lengths) will be used to determine the maximum item!  So max() will 
# then return the longest string in the list.

max_string = max(strings, key = len)

# Output the longest string in the list
print(max_string)