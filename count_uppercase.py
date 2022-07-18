################################################################################
#
# Program: Count Uppercase Characters
# 
# Description: Count the number of uppercase characters in a string with Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=zddF2csxXgM 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Function that returns the number of uppercase characters in the string 'text'
def count_uppercase(text):
  
  # Count will be used to keep track of the number of uppercase characters in
  # the string, we initialize it to 0 as there may be no uppercase characters 
  # in the string...
  count = 0
  
  # The loop body will execute for each character in the string 'text', and we 
  # use the isupper() method to check if that character is uppercase.  If it 
  # uppercase we increment count to keep the count of uppercase characters 
  # encountered in the string up to date.
  for character in text:
    if (character.isupper()):
      count += 1
  
  # After checking each character in the string, count will store the number of 
  # uppercase characters total in the string, and we return this value
  return count


# Prompt the user to enter a string of text, store what they enter into text
text = input("Text: ")

# Call the count_uppercase() function with the text string as an argument to 
# get the count of uppercase characters
count = count_uppercase(text)

# Print out the count of uppercase characters
print("Count:", count)