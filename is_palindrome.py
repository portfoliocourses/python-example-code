################################################################################
#
# Program: Check If A String Is A Palindrome
# 
# Description: A palindrome is a string that is the same as its reverse, i.e. 
# a string that reads the same backwards as it does forwards.  The Python 
# function below will detect if a string is a palindrome or not.
#
# YouTube Lesson: https://www.youtube.com/watch?v=-9degjR16bY 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# returns true if the string text is a palindrome and false otherwise 
def is_palindrome(text):
  
  # find the length of the string, store it into length
  length = len(text)
  
  # compare each character in the string on the left side with its corresponding
  # character on the right side up to the midway point, if a character ever does
  # not match we do not have a palindrome but if all those characters match 
  # than we must have a palindrome
  for i in range(0, length // 2):
    if (text[i] != text[length - i - 1]):
      return False

  return True

# string1 is a palindrome and we expect to get back 'True'
string1 = "racecar"
print(is_palindrome(string1))

# string2 is not a palindrome and we expect to get back 'False'
string2 = "abceba"
print(is_palindrome(string2))