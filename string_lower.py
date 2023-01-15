################################################################################
#
# Program: String lower() Method
# 
# Description: Examples of using the lower() method in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=P7J_jXRIzdU 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Create a test string
string = "Some of the LETTERS are UpperCase"

# The .lower() method will return a new string identical to the original string
# except all uppercase letters will be turned into lowercase letters.  The 
# method will ignore all other characters (numbers, digits, etc.).
new_string = string.lower()

# Output the new string to confirm all letters have been made lowercase
print(new_string)