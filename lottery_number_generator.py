################################################################################
#
# Program: Lottery Number Generator
# 
# Description: Example of how to generate random lottery numbers using Python.
# Lottery number mathematics: https://en.wikipedia.org/wiki/Lottery_mathematics.
# Our program will randomly select some amount of distinct numbers from a 
# range of numbers, e.g. 6 numbers from 1-49, using a range and amount of 
# numbers specified by the user.
#
# YouTube Lesson: https://www.youtube.com/watch?v=t8_T2DwEyvw 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Import the random module so we can use the sample function to randomly 
# select distinct numbers from a range
import random

# Prompt the user to enter the starting point of the range of numbers, convert
# the string they've entered into an int value and store it into start
start = int(input("Start: "))

# In the same way, get the end point of the range from the user
end = int(input("End: "))

# And again in the same way, get the amount of numbers to choose from the 
# range from the user
amount = int(input("Amount Chosen: "))

# It doesn't make any sense to select 0 or less numbers from the range, so exit
# the program with an error message if the amount is less than or equal to zero
if (amount <= 0):
  print("Amount chosen must be at least one!")
  quit()

# It's not possible to randomly select more distinct numbers from a range that 
# exist at all in the range... e.g. we can't randomly select 50 distinct numbers
# from the range 1-49 as there are only 49 numbers total!  If the amount to 
# choose exceeds the available numbers in the range, exit with an error message.
if (end - start + 1 < amount):
  print("Amount chosen can't exceed available numbers!")
  quit()

# The sample function will randomly select amount numbers from the range of 
# numbers from start to end.  We use range(start,end+1) to define the range,
# with end+1, to ensure the range of numbers is inclusive of the end point 'end'
numbers = random.sample(range(start,end+1),amount)

# Output the randomly selected lottery numbers
print(numbers)