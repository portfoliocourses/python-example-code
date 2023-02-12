################################################################################
#
# Program: Fibonacci Sequence Using Recursion
# 
# Description: Calculate the Fibonacci Sequence using a recursive function.  
# See the Wikipedia article on Fibonacci numbers for more information on how 
# the sequence works: https://en.wikipedia.org/wiki/Fibonacci_number.
#
# YouTube Lesson: https://www.youtube.com/watch?v=x2F2BIAB-bs 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################


#  Fibonacci Sequence
#
#  Fn: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
#
#   n: 0  1  2  3  4  5  6  7   8   9   10
#   
#  The Fibonacci sequence is the sequence of above integers Fn, we call each 
#  integer in the sequence term 0, term 1, ... term n.
# 
#  The sequence is defined by the following recurrence relation, where the first
#  two terms in the sequence term 0 and term 1 are the initial conditions 0 and 
#  1, and term n in the sequence is given by the sum of the last two terms in 
#  the sequence.
#
#  F0 = 0
#  F1 = 1
#  Fn = Fn-2 + Fn-1


# The recursive function handles the first two terms by simply returning 0 
# for term 0 and 1 for term 1.  All other terms n > 1 are handled by 
# recursively calling the function with n-2 and n-1 to obtain the last two 
# terms in the sequence, and returning the sum of these terms as the 
# Fibonacci term n.
#
def fib(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n-2) + fib(n-1)


#              fib(3)
#            /      \
#       fib(2)     fib(1)
#      /     \
#  fib(1)    fib(0)
#
#  The above function will result in a "tree" of recursive function calls as 
#  calculating terms n-2 and n-1 may involve further recursive calls, as 
#  calculating fib(2) does in the case of finding fib(3).
#
#  Because there are two recursive function calls we can call this an example 
#  of binary recursion, multiple recursion and/or tree recursion.

# Test out the function by trying to calculate term 8
print( fib(8) )

# Try to output the first 16 terms in the sequence
for n in range(0,16):
    print( fib(n) )