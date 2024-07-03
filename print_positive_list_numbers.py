################################################################################
#
# Program: Print The Positive Numbers In A List
#  
# Description: Program to print the positive numbers in a list using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=JYSyYm48KDA 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A positive number is a number greater than 0.  Here we have a list of numbers
# with 4 positive numbers 67, 78, 33 and 82. 
numbers_list = [-45,0,67,78,33,-45,82] 

# The for loop body will run for each number in the list from -45 to 82.  Each
# time it runs 'number' will be set to the next number in the list.  We check 
# if the number is greater than 0 (i.e. if it is positive) using an if-statement
# and only output the number if it is positive.
for number in numbers_list:
    if number > 0:
        print(number)
