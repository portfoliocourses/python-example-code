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

def create_random_string(length, chars):
    return ''.join([random.choice(chars) for i in range(length)])

# possible_characters = string.ascii_letters 
# possible_characters += string.digits 
# possible_characters += string.punctuation

string_length = int(input("Random String Length: "))
possible_characters = input("Possible Characters: ")

print( create_random_string(string_length, possible_characters) )

# print( string.ascii_letters )
