################################################################################
#
# Program: Count The Letters In A String
#
# Description: Count the total number of letters in a string using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=ogm3IZG8Bf8 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A test string containing 13 letters
text = "Open 24 hours a day"

# A more traditional approach to counting the number of letters in the string 
# would be to use a loop.  We set a count variable initially to zero, then 
# use a for loop to examine each character in the string.  Each time the for
# loop body executes 'c' will be set to the next character in the string, 
# starting with the first character in the string and ending with the last 
# character.  Technically 'c' is a string made up of one character, so we 
# use the string method isalpha() which will return True if 'c' is a letter 
# and False otherwise.  ONLY if the method returns True because the character
# is a letter do we increment count.  So by the end of the loop's execution
# count will store the total count of all letters in the string!

count = 0
for c in text:
    if c.isalpha():
        count += 1

print("Total Letters:", count)


# In this approach we use a list comprehension, where 'c' will be set to each
# character (i.e. string of one character) in the string, and we call the 
# isalpha() method for each character.  This will result in a list made up 
# of the return values of these function calls, i.e. False for non-letter 
# characters and True for letters.  We then use the list method count to 
# count the number of True items in the list, because this is the number 
# of letters in the string.
count = [c.isalpha() for c in text].count(True)

print("Total Letters:", count)