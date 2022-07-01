################################################################################
#
# Program: Number Guessing Game
# 
# Description: A simple number guessing game in Python.  The user attempts to 
# guess a number between 1-100, if they guess too low they are told to guess 
# higher, if they guess too high they are told to guess lower, and the game 
# continues until they guess the correct number.
#
# YouTube Lesson: https://www.youtube.com/watch?v=B2tviDGFq84 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Use the random module to help generate the random number
import random

# randint() will generate a random integer between 1-100, assign it to 'number'
number = random.randint(1,100)

# guess will store the guesses that the user makes
guess = 0

# continue the game until the user guesses correctly
while guess != number:
  
  # prompt the user to enter a guess, the input() function will return the 
  # string the user enters, convert it to an int with int() and assign the 
  # guess to 'guess'
  guess = int(input("Enter Guess: "))
  
  # if the user guesses too lower, tell them to guess higher, if they guess 
  # too high, tell them to guess lower, and if they get it correct tell 
  # them they've won
  if (guess < number):
    print("Guess higher!")
  elif (guess > number):
    print("Guess lower!")
  else:
    print("You won!")