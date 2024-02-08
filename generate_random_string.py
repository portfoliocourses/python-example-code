################################################################################
#
# Program: Generate A Random String
#
# Description: Program to generate a random string using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=A9Px0M1ucQI 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

import random
import string

# Returns a random string of length 'length' made up of the charaters in the 
# string 'chars'.  The list comprehension will produce a a list of length 
# 'length' with each item a string of one character chosen at random from 
# the chars string (random.choice(chars) will return a string of one character
# randomly chose from chars).  We then use the string method .join() to join 
# these list items together into one string separated by the emptry string ''
# (i.e. a join with no separater characters).
#
def create_random_string(length, chars):
    return ''.join([random.choice(chars) for i in range(length)])


# Alternatively we could implement the function like this, beginning with an 
# empty string and then using a loop that will execute length times to 
# concatenate one random character from chars each time to the string, and 
# then returning the completed string.
#
# def create_random_string(length, chars):
#    random_string = ""
#    for i in range(length):
#        random_string += random.choice(chars)
#    return random_string


# Prompt the user for the length of the random string and a string of the 
# possible characters.  We use int() to convert the entered length into an 
# int value as the input() function prompts the user with the text of the 
# provided string and returns the string they enter.
#
string_length = int(input("Random String Length: "))
possible_characters = input("Possible Characters: ")


# Alternatively we could use the constants defined in the string module to 
# build a string of possible characters, in this case all the ascii_letters
# a-z and A-Z, digits 0-9, and punctuation marks.
#
# possible_characters = string.ascii_letters 
# possible_characters += string.digits 
# possible_characters += string.punctuation


# Test function with provided string length and possible characters string
print( create_random_string(string_length, possible_characters) )
