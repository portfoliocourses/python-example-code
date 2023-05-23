################################################################################
#
# Program: Check If A Password Is Valid
# 
# Description: A program to check the validity of a password using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=4S0tmy9iQNw 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################


# Returns True if the password string argument is valid and False otherwise.
# Where a password is considered valid if it...
#
#   - is at least 8 characters in length
#   - contains at least 1 lower case letter
#   - contains at least 1 upper case letter
#   - contains at least one digit
#   - contains at least one symbol
#
def validate_password(password):
    
    # Use the len() function to get the length of the password string and 
    # return False right away if the password length is not sufficient
    if (len(password) < 8):
        return False  
    
    # Variables to keep track of whether or not the password contains a 
    # character from each category.
    has_lower = False 
    has_upper = False 
    has_digit = False 
    has_symbol = False 
   
    # A string containing all the valid symbol characters
    symbols = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    
    # The loop body will run for each character in the password, with the 
    # variable character set to the next character in the string each time.
    # We set the variables above equal to True when we find a character 
    # from the associated category.
    for character in password:

        # islower() returns True if character is a lower case letter, so set
        # has_lower to True if so as we have found a lower case letter
        if character.islower():
            has_lower = True 

        # isupper() returns True if character is an upper case letter, so set
        # has_upper to True if so as we have found an upper case letter
        if character.isupper():
            has_upper = True 

        # isdigit() returns True if character is a digit, so set has_digit to 
        # True if so as we have found a digit
        if character.isdigit():
            has_digit = True 

        # Technically the isdigit() function will return True for some unusual 
        # characters such as superscript ², if we want to strictly allow only
        # the digit characters 0-9 we could use the in operator like this...
        #
        # if character in "0123456789":
        #    has_digit = True 
        
        # The in operator will return true if the character is found in the 
        # symbols string, in which case we have found a valid symbol and we 
        # set has_symbol to True to recognize this
        if character in symbols:
            has_symbol = True 
    
    # Return true if the password has a lower case letter AND it has an 
    # upper case letter AND so on, and false otherwise
    return has_lower and has_upper and has_digit and has_symbol 

# Test out the function by calling it with different strings as arguments

# Invalid - too short
print(validate_password("TryMe!"))

# Valid
print(validate_password("TryMe!2"))

# Invalid - missing a symbol
print(validate_password("TryMe234"))