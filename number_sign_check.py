################################################################################
#
# Program: Check If A Number Is Positive, Negative Or Zero
# 
# Description: Program to check if a number is positive, negative or zero using 
# Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=lGzJ3HUTSic 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Prompt the user to enter a number with the text "Enter Number: ", the input()
# function will return the number entered by the user as a string type value. 
# In order to compare the number to 0 to determine if it is positive, negative
# or zero, it must be a numeric type value.  So we convert the string to a 
# float type value using float() and store the result into number.
number = float(input("Enter Number: "))

# The first branch of the if-elif-else statement checks if the number is 
# negative by checking if it is less than zero, if it is, we output the 
# number is negative using print().  If this condition is not true the condition
# of the elif branch will be checked next, and we check if the number is 
# positive by checking if it is greater than zero.  If it is, we output that 
# the number is positive using print(), if it is not the only possibility left
# is that the number is zero.  The code in the else branch will execute if 
# the elif condition is false, and so we output the number is zero.  Note that 
# the code for each branch is indented, this makes the code a "block" that 
# will execute for the associated branch.
if number < 0:
    print("Number is negative")
elif number > 0:
    print("Number is positive")
else:
    print("Number is zero")