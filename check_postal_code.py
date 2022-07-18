################################################################################
#
# Program: Validate Canadian Postal Code
# 
# Description: Program to validate that a string is a Canadian Postal Code 
# using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=bAct_7oFakQ 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A Canadian Postal Code has the format:
#
# A1A A1A
#
# Where 'A' is a letter and '1' is a digit (0-9).


# Returns true if the string 'code' is a valid Canadian postal code, and false 
# if it is not.  The function works by checking all possibilities that the 
# string could NOT be a valid postal code before returning true only if all 
# checks have 'passed'.
def is_postal_code(code):
  
  # Check that the string contains exactly 7 characters, otherwise return false 
  # as the string cannot be a valid postal code.
  if (len(code) != 7):
    return False 
  
  # Check that the 1st character in the string is a letter, return false if not
  if (not code[0].isalpha()):
    return False 

  # Check that the 2nd character in the string is a digit, return false if not
  if (not code[1] in "0123456789"):
    return False

  # Check that the 3rd character in the string is a letter, return false if not
  if (not code[2].isalpha()):
    return False 

  # Check that the 4th character in the string is a space, return false if not
  if (code[3] != " "):
    return False 

  # Check that the 5th character in the string is a digit, return false if not
  if (not code[4] in "0123456789"):
    return False

  # Check that the 6th character in the string is a letter, return false if not
  if (not code[5].isalpha()):
    return False 

  # Check that the 7th character in the string is a digit, return false if not
  if (not code[6] in "0123456789"):
    return False
  
  # If all of the above 'checks' have passed the string MUST be a valid postal
  # code and so we return true
  return True

# Codes to test the function out... the first code is valid, all others are not
codes = [
  "L4G 6H7",
  "L4G 6H",
  "LTG 6H7",
  "L4G 657"
]

# Go through each code, print it out and the result / return value of passing
# it to our is_postal_code() validator function
for code in codes:
  print(code, is_postal_code(code))