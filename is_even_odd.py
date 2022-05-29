################################################################################
#
# Program: Check If A Number Is Even Or Odd
# 
# Description: Example of checking if a number is even or odd using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=YpOFFCWkhTM 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Prompt the user to enter a number, convert the string returned from input() 
# to an int using int() and store it into the number variable
number = int(input("Enter number: "))

# Even numbers are divisible by 2, which means if we take the number and divide 
# it by 2 we should get 0 remainder.  The modulus operator % in Python returns 
# the remainder of a division operation.  So to check if a number is even we 
# can check to see if the remainder of the number divided by 2 is equal to 0
# with: number % 2 = 0.  We output even if this is true, and odd if it is not 
# as a number that is not even is odd.
if (number % 2 == 0):
  print("Even")
else:
  print("Odd")

# We can create functions to return true or false if a number is even or odd, 
# and vice versa, so that way we can call the functions with different numbers 
# at different points in our program.

# returns true if the number is even and false if it is odd
def is_even(number):
  return number % 2 == 0

# returns true if the number is ODD and false if it is even, as odd numbers will
# have a remainder of 1 when divided by 2
def is_odd(number):
  return number % 2 == 1

# test out the is_even() function
if (is_even(8)):
  print("8 is even")

# test out the is_odd() function
if (is_odd(7)):
  print("7 is odd")