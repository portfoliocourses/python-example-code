################################################################################
#
# Program: Sum Two Numbers From User Input
# 
# Description: Add together two numbers that have been provided from user input
# with Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=X5IMiLsbieM 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Use input() to prompt the user with the text "Number 1: ", the user will then 
# be given a chance to enter in a string.  When the user enters a string and 
# hits enter it will be returned from input, but to get the number value inside 
# of the string we use float() to convert it to a floating-point number (a 
# number that may have decimal places), and we store the result into number1.
number1 = float(input("Number 1: "))

# Do the same thing with number2
number2 = float(input("Number 2: "))

# Sum the numbers
sum = number1 + number2 

# Output the resulting sum
print("Sum:", sum)