################################################################################
#
# Program: String center() Method
# 
# Description: An example of using the string center() method in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=tPRQmer15KQ 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Create a string with the text "text", the string will have a length of 4
string = "text"

# The .center() string method will return a new string with the length provided
# as an argument.  The new string will have the text of the old string centered
# inside of it, and by default the space character will be used as padding on 
# either side of this text to center the text.  If we call center() with the 
# argument 6, this will cause a space character on either side of the original
# string's text in the new string.
new_string = string.center(6)

# The new string will look like this: " text "

# Passing the value 10 will create a new that looks like this: "   text   "
#
# new_string = string.center(10)

# We can modify the fill character if we supply an optional 2nd argument, for
# example this would cause the fill character to be "-" and the new string will
# look like: "---text---"
#
# new_string = string.center(10, "-")

# If the length of the new string provided as an argument is less than the 
# length of the original string, the center() method will return the original 
# string...
#
# new_string = string.center(3, "-")

# Output the new string
print(new_string)

# Output the lengths of the old and new strings so we can see the difference
print("old:", len(string))
print("new:", len(new_string))