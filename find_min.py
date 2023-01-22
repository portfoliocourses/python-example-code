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

# Returns the minimum value in the list supplied as an argument
def find_min(list):

    # Assume that the first element in the list is the minimum value in the list
    min = list[0]

    # Go through the remaining elements in the list, and whenever a value is 
    # encountered that is less than the current min value, make this value 
    # the new min value.
    for number in list:
        if (number < min):
            min = number 

    # By the end of the above loop min will contain the smallest value in the 
    # list and we return that value from the function
    return min

# An example list where 2 is the min value
list = [8,9,4,5,2,6]

# Call the find_min() function with the example list as an argument and output 
# the min value returned from the function
print( find_min(list) )


# Python's built-in min() function will also find the maximum value...
#
# print(min(list))


# We don't need to put the algorithm to find the minimum number in a list inside
# a function, we could just write a simple program like this instead:
#
#
# list = [8,9,4,5,2,6]
#
#  min = list[0]
#  for data in list:
#    if (data > max):
#      min = data
#
# print(min)
