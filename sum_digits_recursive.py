################################################################################
#
# Program: Sum The Digits In An Integer Using Recursion
# 
# Description: Program to sum the digits in an integer using recursion in 
# Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=GktKLZYX8v8 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# We can find the sum of the digits in an integer by dividing the integer by 
# 10, and taking the quotient and dividing it by 10, and continuing this process
# until the quotient is 0.  The remainder of each division operation that it 
# takes for the resulting quotient to reach 0 gives us each digit in the number.
#
# So for example with 472: 
#
# 472 / 10 = 47 remainder 2
#  47 / 10 = 4  remainder 7
#   4 / 10 = 0  remainder 4
#
# And the sum of the remainder 4 + 7 + 2 = 13 is the sum of the digits in
# 472 as 4, 7, and 2 are the digits of the integer.
#
# In Python the integer division operation // give us the quotient of a 
# division operation and the modulus operator % gives us the remainder.
#
# To solve a problem using recursion we will create a recursive function,
# i.e. a function which calls itself.  A recursive function will typically 
# solve part of the problem to be solved and then call itself with a smaller 
# portion of the remaining same problem to be solved.  We have our recursive 
# function sum one digit each time it is called, and call itself with the 
# quotient after diving by 10:
#
# remainder = number % 10
# ...
# return 1 + sum_digits(number // 10) 
#
# We return the result of adding the remainder/digit to the sum of the digits 
# in number // 10 (i.e. the sum of the remaining digits in the number) as 
# given by calling the function sum_digits again with number // 10.  We call 
# this the recursive step or recursive case, where the function calls itself.
#
# We stop recursion when the number divided by 10 results in a quotient of 
# 0, as this tells us we have found the last digit, and we simply return 
# that digit (remainder).
#
# if number // 10 == 0:
#     return remainder
#
# We call this step where recursion stops the base case or the base step.

# Returns the sum of the digits in the integer value number
def sum_digits(number):
    remainder = number % 10
    if number // 10 == 0:
        return remainder 
    return remainder + sum_digits(number // 10)
     
# Test the function
print(sum_digits(472))