################################################################################
#
# Program: Mask A Credit Card
# 
# Description: Program to mask credit card numbers using Python.    
#
# YouTube Lesson: https://www.youtube.com/watch?v=dMO35dBZ8oA 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

import re

# returns a masked credit card string for the string credit_card, leaving 
# unmasked_digits number of digits unmasked and hiding digits using the 
# mask_character.
def mask_credit_card(credit_card, unmasked_digits=4, mask_character='*'):

    # Find the total number of digits in the credit_card string by calling
    # the isdigit() method for each character in the string as part of a 
    # list comprehension... producing a list of True/False values, we then
    # count the number of True values (digits) using the list count() method.
    total_digits = [c.isdigit() for c in credit_card].count(True)

    # It doesn't make any sense to leave more digits unmasked than there are 
    # digits total in the credit card, so if this occurs we should output an
    # error message, raise an exception, or return None, i.e. something to 
    # acknowledge an error has taken place.
    if unmasked_digits > total_digits:
        return None

    # Determine the total number of digits needed to be replaced
    total_replace_digits = total_digits - unmasked_digits 
    
    # Use the sub() function of the regular expression module to replace 
    # total_replace digits number of digits in the string credit_card with 
    # the mask_character, where \\d is a pattern that will match for digits.
    return re.sub("\\d", mask_character, credit_card, total_replace_digits)

# Test the function by masking all but the last 6 digits of credit_card1, the 
# default mask_character of '*' will be used since we don't supply the argument.
credit_card1 = "3776222750878661"
print(mask_credit_card(credit_card1, 6))

# Again test the function by masking all but the last 5 digits of credit_card2,
# this time using the '#' character to mask digits.
credit_card2 = "5545 4234 6381 71925"
print(mask_credit_card(credit_card2, 5, "#"))