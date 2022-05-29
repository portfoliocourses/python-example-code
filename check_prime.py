################################################################################
#
# Program: Check If A Number Is Prime
# 
# Description: Example of checking if a number is prime using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=ZP0QcJrclE4 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################


# prompt the user to enter a number, store the number as an int value
number = int(input("Enter Number: "))

# start off with the assumption the number *is* prime and we'll try to show that
# it is not prime
is_prime = True

# A prime number *must* be > 1
if number > 1:
  
  # A prime number only has 1 and itself as factors, no other factors between 
  # 2 ... number-1 should be found otherwise the number is NOT prime.  A factor 
  # is a number that divides another number with no remainder.  So in this loop
  # we check all possible divisors between 2 and number-1 to see if they are 
  # factors.
  for divisor in range(2, number):

    # The modulus operator % returns the remainder of number divided by divisor,
    # so if the remainder is 0 we know that the divisor is a factor and that the 
    # number is NOT prime.  So we set is_prime to false and stop checking for 
    # factors because finding one is enough to demonstrate the number is not 
    # prime!
    if (number % divisor) == 0:
      is_prime = False
      break
   
  # If after checking all the numbers between 2 and number-1 and NONE of them 
  # are divisors, is_prime will still be true (from when we set it above) and 
  # we can say the number MUST be prime.  Otherwise if we found a factor then 
  # is_prime will be set to false and we can report the number is NOT prime.
  if is_prime:
    print(number, "is prime")
  else:
    print(number, "is not prime")

# if the number is not greater than 1, inform the user 
else:
  print("Number must be > 1")


# We can also define a function that checks whether a number is prime and 
# returns true if the number is prime and false otherwise.  
def check_prime(number):
  
  # The algorithm to determine whether the number is prime is exactly the same 
  # as above, just done within a function!
  is_prime = True
  if number > 1:
    for divisor in range(2, number):
      if (number % divisor) == 0:
        is_prime = False
        break

    # Instead of outputting whether the number is prime, we return true/false
    # whether the number is prime or not
    return is_prime
  
  # if the number is not > 1 we know it is not primve
  else:
    return False


# test the function, 7 should be prime
if (check_prime(7)):
  print("7 is prime")

# test the function, 6 should NOT be prime
if (not check_prime(6)):
  print("6 is NOT prime")
  
  
#    A prime number is a natural number 
#    greater than 1 with only two factors:
#    the number 1 and the number itself.
#
#
#    Natural numbers: 1, 2, 3, ...
#
#
#    A factor is a number that divides
#    another number with no remainder.
#
#
#    So 3 is a factor of 6 because:
#
#      6 / 3 = 2 with 0 remainder
#
#    But 3 is NOT a factor of 7 because:
#
#      7 / 3 = 2 with 1 remainder
#
#
#    A prime number is a natural number 
#    greater than 1 with only two factors:
#    the number 1 and the number itself.
#
#
#    Check if 6 is prime...
#
#    6 / 2 = 3 remainder 0 - 6 is NOT prime 
#    6 / 3 = 2 remainder 0 - 6 is NOT prime
#    6 / 4 = 1 remainder 2
#    6 / 5 = 1 remainder 1
#
#   
#    Check if 7 is prime...
#
#    7 / 2 = 3 remainder 1
#    7 / 3 = 2 remainder 1
#    7 / 4 = 1 remainder 3
#    7 / 5 = 1 remainder 2
#    7 / 6 = 1 remainder 1
#  
#    Because there are NO factors between
#    2 .. 6 we can say that 7 IS prime!
#    
