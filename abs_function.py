################################################################################
#
# Program: Absolute Value Function abs()
# 
# Description: Examples of using the abs() function in Python to find the 
# absolute value of a number, including an example of using the function to 
# find the magnitude of a complex number.
#
# YouTube Lesson: https://www.youtube.com/watch?v=zo8FEfBP2FA 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The absolute value of a number is the non-negative value of the number, i.e.
# the distance of the number from zero.  For example:
#
# |5| = 5
# |-5| = 5
# |0| = 0
# |-2.5| = 2.5

# The abs() function will return the absolute value of an integer argument, 
# so here we'll get back 4 for -4
x = -4
x_abs = abs(x)
print(x_abs)

# The abs() function will return the absolute value of a float argument, 
# so here we'll get back 2.5 for -2.5
y = -2.5
y_abs = abs(y)
print(y_abs)

# The abs() function will return the magnitude of a complex number which is
# the number we get when we sum the square of the real part of the number 
# and the square of the imaginary part of the number and calculate the 
# square root of this sum. 
z = 4 + 16j 
z_abs = abs(z)
print(z_abs)