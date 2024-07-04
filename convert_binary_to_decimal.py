################################################################################
#
# Program: Convert A Binary Number To A Decimal Number
#  
# Description: Program to convert a binary number to a decimal number using 
# Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=E0UoYzma13g
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# To convert a binary number to a decimal number we can sum the "weight" of the 
# digits that are set to 1, knowing that each digit in the binary number 
# is "weighted" an increasing power of 2.
#
#       101011 binary = 43 decimal
#
#       2^5  2^4  2^3  2^2  2^1  2^0
#       |    |    |    |    |    |
#       32   16   8    4    2    1
#       |    |    |    |    |    |
#       1    0    1    0    1    1
#
#       32 + 8 + 2 + 1 = 43  


# This loop will continue so long as the user has not yet provided a valid 
# binary number as input, i.e. a binary string made up of only the characters
# '0' and '1'.
while True:

    # Prompt the user to enter a binary number.  The text the user enters will
    # be returned by the input() function as a string, we convert that string 
    # to a list using list() and store it into binary.  So if the user enters 
    # in the text 101011 binary will be set to a list of strings made up of 
    # one character each, i.e. ['1', '0', '1', '0', '1', '1']
    binary = list(input("Enter Binary Number: "))

    # The all() function will return True if all the items in the list it is 
    # passed as an argument are True, otherwise it will return False.  We 
    # construct a list using a list comprehension which will examine each string
    # 'c' in the list 'binary'.  If that string 'c' is either '0' or '1' (i.e. 
    # is c in the string "01"), then we add a True item to the list being 
    # constructed for that string, otherwise we add a False item to the list.  
    # So the list built by the list comprehension will contain only True items 
    # ONLY if the list 'binary' is made up of only the strings '0' and '1'.  And
    # thus the all() function will only return True in this case as well, 
    # allowing us to verify if the entered string is a binary string or not!  
    #
    # If the string is a valid binary string we stop the loop using 'break', 
    # otherwise we remind the user all digits must be either '0' or '1'.
    #
    if (all([True if c in "01" else False for c in binary])):
        break 
    else:
        print("All digits must be either 0 or 1")


# We'll store the converted decimal number into decimal, which we initialize to
# 0 as we'll add the weight of each digit that is set to '1' to decimal one at a
# time by going through the list 'binary' one item at a time.
decimal = 0

# The loop with execute as many times as there are items in the list 'binary', 
# i.e. or as many digits in our binary number.  And as it does the counter 
# variable i will go from 0, 1, ..., len(binary)-1, where len(binary) is the 
# length of our binary number.  These numbers in the range 0, 1, ..., 5 in 
# the case of 101011 will be exactly the exponents of the powers of 2 for 
# each digit in our binary number.
#
# With each loop iteration, we pop off the LAST digit in the list, so for the 
# list ['1', '0', '1', '0', '1', '1'] we'll pop off 1, then 1, then 0, and so 
# on.  We then check if the digit is 1.  If it is, we get the weight of that 
# digit using pow(2, i), where i the exponent of the power of 2 for that 
# digit, and we add that weight to the decimal number we are creating.
#
# When the loop is done we will have added the weight of all the relevant 
# digits to decimal and the sum and conversion will be complete.
#
for i in range(len(binary)):
    next_digit = binary.pop()
    if next_digit == "1":
        decimal += pow(2, i)

# Output the converted decimal number
print(decimal)
