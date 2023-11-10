################################################################################
#
# Program: Count The Digits In An Integer Using Recursion
# 
# Description: Program to count the digits in an integer using recursion in 
# Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=CTqMbOTGnDI 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# We can find the number of digits in an integer by dividing the integer by 
# 10, and taking the quotient and dividing it by 10, and continuing this process
# until the quotient is 0.  The number of divisions that it takes for the 
# resulting quotient to reach 0 is the number of digits in the number.
#
# So for example with 472: 
#
# 472 / 10 = 47 remainder 2
#  47 / 10 = 4  remainder 7
#   4 / 10 = 0  remainder 4
#
# And because we have 3 division operations this tells us the number has 3 
# digits.
#
# To solve a problem using a recursion we will create a recursive function,
# i.e. a function which calls itself.  A recursive function will typically 
# solve part of the problem to be solved and then call itself with a smaller 
# portion of the remaining same problem to be solved.  We have our recursive 
# function count one digit each time it is called, and call itself with the 
# quotient after diving by 10:
#
# return 1 + count_digits(number // 10) 
#
# We add 1 to the count of the number of digits of number // 10 as returned by 
# calling the function, in order to return the total number of digits in the
# number.  Note that // is integer division in Python and will return the 
# quotient of the number divided by 10.  We call this the recursive step or 
# recursive case, where the function calls itself.
#
# We stop recursion when the number divided by 10 results in a quotient of 
# 0, as this tells us we have counted the last digit and we simply return 1.
#
# if number // 10 == 0:
#     return 1
#
# We call this step where recursion stops the base case or the base step.


# Returns the number of digits in the integer 'number' using recursion
def count_digits(number):
    if number // 10 == 0:
        return 1
    return 1 + count_digits(number // 10) 
 
# Test the function 
print(count_digits(472))