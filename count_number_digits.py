################################################################################
#
# Program: Count The Number Of Digits In A Number
#
# Description: Program to count the number of digits in a number using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=XC1R6nKJYPE 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

def digit_counter(number):

    number = abs(number)
    count = 0

    while number != 0:
        number //= 10
        count += 1

    return count 

print("Digit Total:", digit_counter(-123))