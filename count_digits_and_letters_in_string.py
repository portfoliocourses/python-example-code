################################################################################
#
# Program: Count The Digits And Letters In A String
#
# Description: Count the total number of digits and letters in a string using 
# Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=B8Cd2AH1lIE 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns the total number of letters and digits in the string 'text'
def count_letters_and_digits(text):

    # Variables will store the running counts of letters and digits found
    total_letters = 0
    total_digits = 0
    
    # Loop body will execute for each character in the string text, with c set
    # to a string made up of that one character.  We use the isalpha() method 
    # and isdigit() string methods to check if the character is a letter or
    # digit respectively, and increment the correct running counts if so. 
    for c in text:
        if c.isalpha():
            total_letters += 1
        elif c.isdigit():
            total_digits += 1
    
    # We use the , to return two values from the function (both counts)
    return total_letters, total_digits

# Test string with 2 digits and 13 letters
text1 = "Open 24 hours a day"

# Test the function, store the values returned into ltotal and dtotal
ltotal, dtotal = count_letters_and_digits(text1)

# Output the totals
print("Total Digits:", dtotal)
print("Total Letters:", ltotal)