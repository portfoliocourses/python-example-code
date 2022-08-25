################################################################################
#
# Program: Dice Roll Simulator
# 
# Description: Example of how to simulate a dice roll in Python, for any number
# of dice and any number of sides per dice.
#
# YouTube Lesson: https://www.youtube.com/watch?v=bsIYU_q5g7Y 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# We import the random module so we can use the randint() function to generate 
# random integers in a given range
import random

# Returns a list containing the results of a dice roll, where we have dice 
# number of elements set to randomly selected values between 1 ... sides
def dice_roll(dice, sides):
  
  # We start off with an empty list
  roll = []
  
  # We create a loop that will execute 'dice' number of times, to roll each 
  # dice.  We use the randint() method of the random module to obtain a random
  # integer between 1 and sides, the 'face' of the dice that has been 'rolled'.
  # We then append this new result to the roll list.
  for i in range(0,dice):
    face = random.randint(1,sides)
    roll.append(face)
  
  # Return the now complete list of dice roll results
  return roll

# Prompt the user to enter the number of dice to be rolled, convert the string 
# entered into an int, and store the int into the dice variable
dice = int(input("Dice: "))

# We can't roll the dice if there isn't at lesat one dice, so if the dice 
# integer is less than or equal to zero we exit the program with an error 
# message.
if (dice <= 0):
  print("Must have at least one dice!")
  quit()

# Prompt the user to enter the number of sides per dice, convert the string 
# entered into an int, and store the int into the sides variable
sides = int(input("Sides: "))

# We can't roll a dice if there isn't at least 1 side, so if the sides 
# integer is less than or equal to zero we exit the program with an error 
# message.
if (sides <= 0):
  print("Must have at least one side!")
  quit()

# Perform the dice roll using the dice_roll() function, passing the dice and 
# sides value provided by the user as arguments, assign the list returned to 
# roll
roll = dice_roll(dice, sides)

# Print out the result of the dice roll
print(roll)