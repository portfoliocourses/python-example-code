################################################################################
#
# Program: Count Lowercase Characters
# 
# Description: Count the number of lowercase characters in a string with Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=KjSt3gXSCSY 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Function that returns the number of lowercase characters in the string 'text'
def count_lowercase(text):
  
  # Count will be used to keep track of the number of lowercase characters in
  # the string, we initialize it to 0 as there may be no lowercase characters 
  # in the string...
  count = 0
  
  # The loop body will execute for each character in the string 'text', and we 
  # use the islower() method to check if that character is lowercase.  If it 
  # lowercase we increment count to keep the count of lowercase characters 
  # encountered in the string up to date.
  for character in text:
    if (character.islower()):
      count += 1
  
  # After checking each character in the string, count will store the number of 
  # lowercase characters total in the string, and we return this value
  return count


# Prompt the user to enter a string of text, store what they enter into text
text = input("Text: ")

# Call the count_lowercase() function with the text string as an argument to 
# get the count of lowercase characters
count = count_lowercase(text)

# Print out the count of lowercase characters
print("Count:", count)