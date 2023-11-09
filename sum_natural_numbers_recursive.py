################################################################################
#
# Program: Sum The First N Natural Numbers Using Recursion
# 
# Description: Program to sum the first N natural numbers using recursion in 
# Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=skUMJwu1-aQ
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The natural numbers are the numbers 1,2,3,...
#
# So the first 5 natural numbers and their sum are 5 + 4 + 3 + 2 + 1 = 15
#
# A recursive function is a function that calls itself to solve a problem, 
# typically solving part of the problem and calling itself with a smaller 
# version of the remaining problem to be solved.
#
# The below function carries out the chain of addition operations required 
# to produce the sum, by returning 'n' the current natural number + the 
# result of calling the function with 'n-1'.  This will result in a chain 
# of additions as each function call returns 5 + 4 + 3 + ..., etc.
#
# We call the "return n + sum(n-1)" case the recursive case or recursive step.
# Eventually recursion (the function calling itself) needs to stop.  We stop
# recursion and simply return 1 once n == 1, as 1 is the final natural 
# number.  We call this case where recursion stops the base case or the 
# base step.

# Returns the sum of the first n natural numbers using recursion
def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)    

# Test the function
print(sum(5))

# We can visualize the series of function calls that will occur like this...
#
# sum(5) -> return 5 + sum(4)
# sum(4) -> return 4 + sum(3)
# sum(3) -> return 3 + sum(2)
# sum(2) -> return 2 + sum(1)
# sum(1) -> return 1             (special base case where recursion stops)

# We can then work backwards from the bottom to the top, replacing each
# function call with the relevant return value, and we see how the sum(5)
# will return 15...
#
# sum(5) -> return 5 + 10 -> return 15
# sum(4) -> return 4 + 6 -> return 10
# sum(3) -> return 3 + 3 -> return 6
# sum(2) -> return 2 + 1 -> return 3
# sum(1) -> return 1