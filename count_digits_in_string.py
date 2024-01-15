################################################################################
#
# Program: Count The Digits In A String
#
# Description: Count the total number of digits in a string using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=w5y6FFJFsqs 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A test string containing 3 digits: 2, 4 and 7
text = "Open 24 hours a day, 7 days a week"

# A more traditional approach to counting the number of digits in the string 
# would be to use a loop.  We set a count variable initially to zero, then 
# use a for loop to examine each character in the string.  Each time the for
# loop body executes 'c' will be set to the next character in the string, 
# starting with the first character in the string and ending with the last 
# character.  Technically 'c' is a string made up of one character, so we 
# use the string method isdigit() which will return True if 'c' is a digit 
# and False otherwise.  ONLY if the method returns True because the character
# is a digit do we increment count.  So by the end of the loop's execution
# count will store the total count of all digits in the string!

count = 0
for c in text:
    if c.isdigit():
        count += 1

print("Total Digits:", count)


# In this approach we use a list comprehension, where 'c' will be set to each
# character (i.e. string of one character) in the string, and we call the 
# isdigit() method for each character.  This will result in a list made up 
# of the return values of these function calls, i.e. False for non-digit 
# characters and True for digits.  We then use the list method count to 
# count the number of True items in the list, because this is the number 
# of digits in the string.
count = [c.isdigit() for c in text].count(True)

print("Total Digits:", count)