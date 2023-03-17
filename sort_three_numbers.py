################################################################################
#
# Program: Sort Three Numbers Without Using sort()
# 
# Description: A program to sort 3 numbers in Python without using sort() or 
# similar sorting helper functions such as max, min, swap, etc.
#
# YouTube Lesson: https://www.youtube.com/watch?v=I2xbPMXfA8Q 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Prompt the user to enter 3 numbers and store them into variables n1, n2 and n2
n1 = float(input("Enter Number 1: "))
n2 = float(input("Enter Number 2: "))
n3 = float(input("Enter Number 3: "))

# There are only 6 possible orders for 3 numbers.  Either n1, n2 or n3 is the
# smallest number.  And if n1 is the smallest number, either n2 is the middle 
# number (and n3 is the highest number) or n3 is the middle number (and n2 
# is the highest number).  If n2 is the smallest number, either n1 is the middle
# number (and n3 is the highest number) or n3 is middle number (and n1 is the 
# highest number).  If n3 is the smallest number, either n2 is the middle number
# (and n1 is the highest number) or n1 is the middle number (and n3 is the 
# highest number).
#
# These possible orders are expressed below:
#
#  n1 <= n2 and n3
#        n2 <= n3
#        n3 <= n2 
#  n2 <= n1 and n3
#        n1 <= n3
#        n3 <= n1
#  n3 <= n1 and n2
#        n1 <= n2
#        n2 <= n1
#
# When we layout the possible orders like this, we may be able to see a solution
# to the problem!
#
# We'll use an outer if-elif-else statement to determine which of n1, n2 or n3
# is the lowest number.  We'll then use nested if-else statements to determine 
# which of the two remaining numbers is the middle number and which is the 
# highest number.  We'll store the lowest, middle and highest numbers into 
# variables with these names
#
# See the implementation of exactly this algorithm below...
#

# case that n1 is the lowest
if (n1 <= n2 and n1 <= n3):

    lowest = n1 
    
    # decide which of n2 or n3 is the middle and highest (two possibilities)
    if (n2 <= n3):
        middle = n2 
        highest = n3 
    else:
        middle = n3 
        highest = n2 

# case that n2 is the lowest
elif (n2 <= n1 and n2 <= n3):

    lowest = n2

    # decide which of n1 or n3 is the middle and highest (two possibilities)
    if (n1 <= n3):
        middle = n1
        highest = n3 
    else:
        middle = n3 
        highest = n1 

# case that n3 is the lowest
else:

    lowest = n3 

    # decide which of n1 or n2 is the middle and highest (two possibilities)
    if (n1 <= n2):
        middle = n1 
        highest = n2 
    else:
        middle = n2 
        highest = n1 


# Output the 3 numbers in ascending order
print("asc:", lowest, middle, highest)

# Output the 3 numbers in descending order
print("desc:", highest, middle, lowest)