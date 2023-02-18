################################################################################
#
# Program: String replace() Method
# 
# Description: Examples of using the string replace() method in Python to 
# replace occurrences of a substring in a string with another substring.
#
# YouTube Lesson: https://www.youtube.com/watch?v=M5MTjFhTFVY 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Will replace all occurrences of the substring "best" in the string text with 
# the substring "worst".  The call to .replace() does not modify the original 
# string, it creates and returns a new string.
text = "best of the best"
new_text = text.replace("best", "worst")
print(new_text)

# We can optionally provide a 3rd argument for the number of occurrences of the
# substring to replace.  In the below call to .replace(), only the first 
# occurrence of the substring "best" will be replaced with "worst".
text = "best of the best"
new_text = text.replace("best", "worst", 1)
print(new_text)

# In the below call to .replace(), both occurrences of the substring "best" 
# will be replaced with the substring "worst".
text = "best of the best"
new_text = text.replace("best", "worst", 2)
print(new_text)