################################################################################
#
# Program: Calculate The Factorial Of A Number
#  
# Description: Program to calculate the factorial of a number using Python. For
# the definition of a factorial see: https://en.wikipedia.org/wiki/Factorial
#
# YouTube Lesson: https://www.youtube.com/watch?v=tDTQ1h40SwE 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The factorial of a non-negative integer n is defined as the product of all 
# positive integers between n an 1, with the factorial of 0 defined as 1.
#
# n! = n x n-1 x .. x 2 x 1
#
# 5! = 5 x 4 x 3 x 2 x 1 = 120
#
# 0! = 1

# The math module includes a factorial function
import math

# Or we can create our own.  This function returns the factorial of n by 
# calculating the product of all integers between n and 1.  It uses a 
# loop and counter variable to go through all of these integers, building
# the product one multiplication at a time using 'product'.  Notably 
# the function will still work for 0! n=0 as product is set to 1 and the
# loop will not execute at all in this case so we simply return 1.
def factorial(n):
    product = 1 
    for i in range(1,n+1): 
        product *= i
    return product

# Prompt the user to enter n, convert the string into an int type value and 
# store it into n
n = int(input("Enter n: "))

# Output an error message if n is not a non-negative integer, otherwise we 
# call the factorial function to calculate the product and output the result
if n < 0:
    print("n must be a non-negative integer")
else:
    product = factorial(n)
    print(product)

# We could also use the math module's factorial function
print(math.factorial(5))