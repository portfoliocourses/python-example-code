################################################################################
#
# Program: Check If A String Is A Binary String
#  
# Description: Program to check if a string is a binary string using Python. 
# i.e. the program will check if the string is a binary number containing only 
# '0' and '1' digits (characters).
#
# YouTube Lesson: https://www.youtube.com/watch?v=Z79zHhFb1So
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Prompt the user to enter a potential binary number, store the entered text 
# as a string into the variable binary
binary = input("Enter Binary Number: ")

# The all() function will return True if all the items in the list it is passed 
# as an argument are True, otherwise it will return False.  We construct a list 
# using a list comprehension which will examine each character 'c' in the binary
# string.  If that character 'c' is either '0' or '1' (i.e. is c in the string 
# "01"), then we add a True item to the list being constructed for that 
# character, otherwise we add a False item to the list.  So the list built by 
# the list comprehension will contain only True items ONLY if the string is 
# made up of only '0' and '1' digits (characters).  And thus the all() function
# will only return True in this case as well, allowing us to verify if the 
# the string is a binary string or not!  
#
if all([True if c in "01" else False for c in binary]):
    print("Binary String")
else:
    print("Not A Binary String")