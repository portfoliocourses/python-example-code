################################################################################
#
# Program: Remove All Punctuation Marks From A String
# 
# Description: Program to remove all punctuation marks from a string in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=zo8FEfBP2FA 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

import string

# Test string with some punctuation marks
text = "Should, 'we' use; punctuation marks...?!"

# The string module contains a punctuation string constant containing all the 
# punctuation marks
print(string.punctuation)

# The string method translate can use a translation table passed in an as 
# argument that is created by the method maketrans to replace and remove 
# characters in a string.  To make the translation table, we pass in empty 
# strings for the first two arguments as we don't need to replace any characters
# in the string (and that is what these arguments can help do), but we do pass 
# the optional 3rd argument... a string of all the characters to remove, in 
# this case, string.punctuation (i.e. all the punctuation marks).  The 
# translate method will produce a new string.
new_text = text.translate(str.maketrans('','',string.punctuation))

# Output the new string
print(new_text)