################################################################################
#
# Program: String lfill() rfill() Methods
# 
# Description: Examples of using the lfill() and rfill() string methods in 
# Python to left justify and right justify a string.
#
# YouTube Lesson: https://www.youtube.com/watch?v=nT3tuBSk7G4 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# rjust() will return a new string of length 10 characters with the original 
# string right-justified within it, and the blank space ' ' character will 
# be used as padding by default for the unused characters of the new string.
string = "text"
right_justified = string.rjust(10)
print(right_justified)

# We can provide another argument to change the fill character used for 
# padding, below the * character will be used as padding instead of ' '.
string = "text"
right_justified = string.rjust(10, "*")
print(right_justified)

# If the length provided is less than the original string, the string will not
# be truncated, the method will return the original string.
string = "text"
right_justified = string.rjust(3, "*")
print(right_justified)

# ljust() works exactly like rjust() except it will left justify the string.
string = "text"
left_justified = string.ljust(10, "*")
print(left_justified)

# Notably there is also a center() method that will center a string, equally 
# distributing the fill character to the left and right of the original string
# to center it within the new string.
string = "text"
centered = string.center(10, "*")
print(centered)