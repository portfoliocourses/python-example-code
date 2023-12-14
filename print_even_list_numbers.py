################################################################################
#
# Program: Print Even Numbers In A List
#
# Description: A program to compute the even numbers in a list using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=jWsx8C_uVCo
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Create a test list with the integers from 1 - 10
listA = [1,2,3,4,5,6,7,8,10]

# A number is considered even if it is divisible by 2, which means if we take
# the number and divide it by 2 it has zero remainder.  We use a for loop to
# check each number in the list... this loop body will execute for each
# element in the list, and the first time it executes 'number' will be set to
# '1' and the next time it executes 'number' will be set to '2', and so on.
# The modulus operator % will give us the remainder of a division operation, so
# we then check using an if-statement if the number is divisible by 2 with
# "number % 2 == 0" (i.e. does the number divided by 2 have a remainder of 0?).
# Only if this is true do we output the number, as the call to print with number
# is in the if-statement body.
# 
for number in listA:
    if (number % 2 == 0):
        print(number)
