################################################################################
#
# Program: Jumbled Word Game
# 
# Description: Example of a jumbled word game in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=O2xrxU0YB6s 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

import random

words = ["python", "coding", "almost",
         "before", "attack", "chance"]

word = random.choice(words)

letters = list(word)
random.shuffle(letters)
jumbled_word = "".join(letters)

print("Unscramble...", jumbled_word)

while True:
    guess = input("Guess: ")
    if guess.lower() != word.lower():
        print("Incorrect try again!")
    else:
        break

print("Congratulations!")