################################################################################
#
# Program: Fizz Buzz Problem
#
# Description: An example of how to solve the Fizz Buzz Problem in Python, a 
# common coding interview question.  See the description of the Fizz Buzz 
# problem and related ideas in the comment at the end of the file.
#
# YouTube Lesson: https://www.youtube.com/watch?v=4pJzmDbqN7U 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# We solve the problem by first creating a loop with a range function that will 
# execute for n = 1, then n = 2, all the way to n = 100.  We use an if-elif-else
# control structure, where the "default" else case is to just print out the 
# number.  We check with the if and elif conditions where the number n is 
# a multiple of 3, 5, as well as 3 AND 5 using the modulus operator to help us.
# The modulus operator % returns the remainder of a division operation, so 
# n % 3 will give the remainder of n divided by 3.  If n % 3 == 0 this means 
# the remainder of n divided by 3 is 0, and so in this case we print out "Fizz".
# The order in which we check th conditions is very important, this is actually
# a common mistake programmers make when attempting to solve this problem 
# during coding interviews.  We check if n is a multiple of 3 AND 5 FIRST.  The 
# issue with checking if n is a multiple of 3 first, or if n is a multiple of 5
# first, is that if these conditions are true we will NEVER reach the "and" 
# case where we check for if both conditions are true, and "FizzBuzz" will 
# never be output.  To see what is meant by this, try swapping the condition of 
# the if-case and the 2nd elif-case!

for n in range(1,101):
  if (n % 3 == 0 and n % 5 == 0):
    print("FizzBuzz")
  elif (n % 3 == 0):
    print("Fizz")
  elif (n % 5 == 0):
    print("Buzz")
  else:
    print(n)
    

#  FizzBuzz Problem: Write a program that prints the numbers from 1 to 100. But 
#  for multiples of three print "Fizz" instead of the number and for the 
#  multiples of five print "Buzz".  For numbers which are multiples of both 
#  three and five print "FizzBuzz".
#  
#  Multiples of 3: 3, 6, 9, 12, 15*, ...
#
#  Multiples of 5: 5, 10, 15*, 20, 25, ...
#
#  Some numbers like 15 are multiples of both 3 and 5.
#
#  If we divide 3 by a number and there is no remainder that number is a multiple 
#  of 3.  Finding a multiple of 5 (or any other number) works the same way.
#
#  FizzBuzz Sequence...
#
#  1
#  2
#  Fizz
#  4
#  Buzz
#  Fizz
#  7
#  8
#  Fizz
#  Buzz
#  11
#  Fizz
#  13
#  14
#  FizzBuzz
#  16
#  ...
