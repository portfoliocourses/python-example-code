################################################################################
#
# Program: Count The Vowels In A String
# 
# Description: A program to count the number of vowels in a string with Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=1KzaruXkDkI 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns the number of vowels in the string 'text'
def count_vowels(text):
  
  # count will be used to keep a running count of the number of vowels in the 
  # string 'text'
  count = 0
  
  # The for loop will execute for each character in the string.  We use the 
  # 'in' operator to check if the character is in a string that is made up 
  # of exactly the vowels (uppercase and lowercase), and if it is then it 
  # must be a vowel so we increment the count.
  for character in text:
    if (character in "aAeEiIoOuU"):
      count += 1
  
  # By the end of the loop count will contain a count of all the vowels in 
  # the string so we return the count.
  return count 

# Prompt the user to enter in a string, store the string entered into 'text'
text = input("Text: ")

# Call the count_vowels() function with the provided string and store the count
# of vowels returned by the function into count.
count = count_vowels(text)

# Output the count value prefixed with the text "Count: "
print("Count:", count)