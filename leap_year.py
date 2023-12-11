################################################################################
#
# Program: Check If A Year Is A Leap Year
# 
# Description: Program to check if a year is a leap year using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=Z95edKacyp4
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A year is a leap year if it is:
#
# 1) divisible by 4 but NOT divisible by 100
#
# OR 
#
# 2) divisible by 400
#
# Where if a year is divisible by a number it means that the year divided 
# by the number has a remainder of 0.  So 2024 is divisible by 4 because:
# 
# 2024 / 4 = 506 remainder 0
#
# But 2023 is NOT divisible by 4 because:
#
# 2023 / 4 = 505 remainder 3
#
# The modulus operator % in Python returns the remainder of a division 
# operation, so if we have year % 4 == 0 this would be true if the year 
# is divisible by 4 and false otherwise.
#
# We use this to create a function to check if a year is a leap or not by 
# checking if the year is divisible or not divisible by numbers according
# to the above definition of a leap year.
#

# Returns True if year is a leap year and False otherwise
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# Prompt the user to enter a year, convert the string entered into an int value
# and store it into year
year = int(input("Enter Year: "))

# Call the function to check if the year is a leap year, output appropriate 
# text accordingly
if is_leap_year(year):
    print(year, "is a leap year") 
else:
    print(year, "is not a leap year")

# for loop will run for year = 2020,2021,...,2040, and we output if each year
# in this range is a leap year or not
for year in range(2020,2041):
    if is_leap_year(year):
        print(year, "is a leap year") 
    else:
        print(year, "is not a leap year")