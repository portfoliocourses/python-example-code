################################################################################
#
# Program: Sum The Digits In A String
#
# Description: Functions to sum the digits in a string using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=AoHjSi-0-BA 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns the sum of the digits in the string text
def sum_digits(text):
   
    # Used to sum the digits, initialized to 0 as no digits have been looked at
    total = 0
    
    # Loops through each character in the string text, where with each loop 
    # iteration 'character' will be set to a string made up of only the next 
    # character in the string.  We use the string method isdigit() to check if 
    # that character is a digit as the method will return True if it is and 
    # False otherwise.  Only if that character is a digit do we use int() to 
    # return the integer value of that digit, which we then add to total.
    for character in text:
        if character.isdigit():
            total += int(character)
    
    # After adding together all the digit values we can return the total
    return total

# Returns the sum of the digits in the string text using a list comprehension
def sum_digits2(text):

    return sum([int(c) for c in text if c.isdigit()])

    # The list comprehension [int(c) for c in text if c.isdigit()] produces a
    # list.  Each character 'c' in the string text is checked to see if it is a
    # digit using isdigit(), and ONLY if it is a digit is the character 
    # converted to an integer value using int() and included in the produced 
    # list as an item.  
    #
    # We then use the built-in sum function to return the sum of the numbers
    # in this list, which we then return from the function as the sum of all
    # digits in the string text.


# Test string
test_string = "A12,X 53c2"

# Test the first function
digit_sum = sum_digits(test_string)
print(digit_sum)

# Test the second function
digit_sum = sum_digits2(test_string)
print(digit_sum)