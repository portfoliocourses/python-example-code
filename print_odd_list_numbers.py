################################################################################
#
# Program: Print Odd Numbers In A List
#
# Description: A program to print the odd numbers in a list using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=B56J6p_v_zY
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A list of numbers
numbers = [7,8,9,10,11,12,13,14,15,16,17]

# If we divide odd numbers such as 7 and 9 by 2 we will get a remainder of 1.
#
# 7 / 2 = 3 remainder 1
# 8 / 2 = 4 remainder 0
# 9 / 2 = 4 remainder 1
#
# The modulus operator in Python % will give us the remainder of a division 
# operation, so for example 9 % 2 gives us back 1...
#
# 9 % 2 == 1

# Loop through each number in the list, check if it odd, and print it if so.
#
# With each iteration of the loop 'number' will be set to the next number in 
# the numbers list.  We use number % 2 to get the remainder of dividing the 
# number by 2, and if it is equal to 1 we output the number.
#
for number in numbers:
    if number % 2 == 1:
        print(number)