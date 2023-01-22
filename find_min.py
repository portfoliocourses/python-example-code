################################################################################
#
# Program: Find The Minimum Number In A List WITHOUT Using min().
# 
# Description: How to find the smallest value in a list in Python without using
# the built-in min() function.
#
# YouTube Lesson: https://www.youtube.com/watch?v=Qe8Q8dQRIJY 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

def find_min(list):

    min = list[0]

    for number in list:
        if (number < min):
            min = number 

    return min

list = [8,9,4,5,2,6]

print( find_min(list) )