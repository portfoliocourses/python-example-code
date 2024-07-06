################################################################################
#
# Program: Count The Number Of Even Numbers In A List
#  
# Description: Program to count the number of even numbers in a list using 
# Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=eScKNNcztEs 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns the number of even numbers in numbers_list
def count_even(numbers_list):

    # An even number is an integer which is divisible by 2, i.e. we take the 
    # number and divide it by 2 we should have a remainder of 0.  The modulus 
    # operator % will give us the remainder of a division operation.
    #
    # We count the number of even numbers in the list by using a for loop to 
    # iterate over each item in the list (which we call 'number').  We use 
    # the modulus operator to check if the number is even by checking to see 
    # if the number divided by 2 gives us a remainder of 0.  Only if the number
    # is even do we increment a running count of the number of even numbers 
    # in the list (total_even).  By the time the loop is done we will have 
    # counted all the even numbers in the list and we then return that count.
    #
    total_even = 0
    for number in numbers_list:
        if number % 2 == 0:
            total_even += 1
    return total_even

# A test list with 4 even numbers: 2,6,4,10
numbers_list = [2,6,7,9,3,4,10,11,15]

# Test the function, output the return value
print(count_even(numbers_list))
