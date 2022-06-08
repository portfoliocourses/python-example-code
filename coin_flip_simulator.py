################################################################################
#
# Program: Coin Flip Simulator
# 
# Description: Example of a coin flip simulator in Python (i.e. coin toss 
# function).
#
# YouTube Lesson: https://www.youtube.com/watch?v=FqfRhnbSdf8 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# we'll use the choice method from the random module to randomly 'flip a coin'
import random

# returns either a "Heads" or "Tails" string randomly
def flip_coin():
  # the choice method will randomly return one of the elements in the list it is
  # passed as an argument, we can then return this value
  return random.choice(["Heads", "Tails"])

# test the function out by printing out the return value
print(flip_coin())

# we could perform a sequence of 10 coin flips using a loop
for i in range(10):
  print("Flip " + str(i+1) + ": " + flip_coin())

# prompt the user for the number of flips they would like to see occur
flips = int(input("Flips: "))

# we'll keep track of the total number of heads and tails that result using 
# these variables
total_heads = 0
total_tails = 0

# perform 'flips' number of flips, and keep track of the number of heads and 
# tails that occur
for i in range(flips):
  # if the flip result is Heads increment the heads count
  if (flip_coin() == "Heads"):
    total_heads += 1
  # if the flip result was not heads, we know it was tails and increment the 
  # tails count 
  else:
    total_tails += 1

# output the total number of heads and tails flips that have occurred
print("Total Heads: " + str(total_heads))
print("Total Tails: " + str(total_tails))