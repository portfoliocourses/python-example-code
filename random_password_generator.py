################################################################################
#
# Program: Random Password Generator
# 
# Description: Example of generating a random password in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=fsjXq2XURTY 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

import random
import string

# Prompt the user to enter the length of the password to generate, store the 
# length entered by the user into length after converting it to an int
length = int(input("Enter Length: "))

# The string module contains strings constants for groups of characters such 
# as punctuation marks, ascii letters and digits.  These groups of characters 
# are the groups of characters typically allowed in a password.  We concatenate
# together these strings to create a string made up of the possible characters 
# our password may contain.  We'll randomly choose characters from this string 
# to build our password.
chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

# Begin the password as an empty string
password = ""

# The loop will run 'length' number of times, and with each iteration we 
# randomly select a character from the string chars using the choice function
# of the random module, and we concatenate it to password.  This will give us
# a string of random characters with the desired length.  
for i in range(length):
    password += random.choice(chars)

# We could alternatively create the random password in one line using a list
# comprehension.  The list comprehension here that is an argument of the join
# string method will give us a list with 'length' number of elements, each of 
# which is a character chosen at random from chars (technically, each element
# is a string of one character).  The join string method will then join these
# string together, separated by '' nothing, to give us our password.
password = ''.join([random.choice(chars) for i in range(length)])

# Output the randomly generated password
print("Your random password is:", password)
