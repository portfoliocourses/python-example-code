################################################################################
#
# Program: divmod() Function
# 
# Description: Examples of using the divmod() function in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=7xoHgWW67-g 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# divmod() will return both the quotient and the remainder of a division 
# operation as a tuple... here quotient will be set to 3, and remainder will be 
# set to 1
quotient, remainder = divmod(10,3)
print("quotient:", quotient)
print("remainder:", remainder)

# If one of the arguments to divmod() is a floating-point number the quotient 
# and remainder will be floating-point numbers.
quotient, remainder = divmod(13,2.5)
print("quotient:", quotient)
print("remainder:", remainder)

# As usual with division, we cannot divide by zero, we will get the 
# ZeroDivisionError as a result if we try.
quotient, remainder = divmod(13,0)
print("quotient:", quotient)
print("remainder:", remainder)