################################################################################
#
# Program: Count The Positive, Negative And Zero Numbers In A List
#  
# Description: Program to count the positive, negative and zero numbers in a 
# list using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=x60vsih56fg
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A test list of numbers with 4 positive numbers, 3 negative numbers and 2 
# zero numbers.  Where positive numbers are > 0, negative numbers are < 0 and
# zero numbers are = 0.
numbers_list = [5,0,-67,85,62,-43,0,1,-6]  

# Maintain "running counts" of the number of positive, negative and zero numbers
# in the list.  Initialized to zero as before we begin counting the types of 
# numbers have not found any number of any type yet.
positive_count = 0
negative_count = 0
zero_count = 0

# Loops through the list of the numbers in the list in order, with each loop 
# iteration 'number' will be set to the next number in the list.  We check 
# to see if the number is positive, negative or zero, and increment the 
# correct running count variable accordingly.  When the loop has finished 
# executed we will have counted all the positive, negative and zero numbers.
for number in numbers_list:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

# Output the resulting counts
print("Positives:", positive_count)
print("Negatives:", negative_count)
print("Zeros:", zero_count)