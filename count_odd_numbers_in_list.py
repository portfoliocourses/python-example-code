################################################################################
#
# Program: Count The Number Of Odd Numbers In A List
#  
# Description: Program to count the number of odd numbers in a list using 
# Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=i1LmlxdogEY 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns the number of odd numbers in numbers_list
def count_odd(numbers_list):

    # An odd number is an integer which when divided by 2 will have a remainder
    # of 1.  The modulus operator % will give us the remainder of a division 
    # operation.
    #
    # We count the number of odd numbers in the list by using a for loop to 
    # iterate over each item in the list (which we call 'number').  We use 
    # the modulus operator to check if the number is odd by checking to see 
    # if the number divided by 2 gives us a remainder of 1.  Only if the number
    # is odd do we increment a running count of the number of odd numbers 
    # in the list (total_odd).  By the time the loop is done we will have 
    # counted all the odd numbers in the list and we then return that count.
    #
    total_odd = 0
    for number in numbers_list:
        if number % 2 == 1:
            total_odd += 1
    return total_odd

# A test list with 3 odd numbers: 3,5,9
numbers_list = [3,5,4,8,6,10,2,9,12]

# Test the function, output the return value
print(count_odd(numbers_list))