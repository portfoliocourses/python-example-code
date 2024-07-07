################################################################################
#
# Program: Count Even And Odd Numbers In A List
#  
# Description: Program to count the number of even and odd numbers in a list 
# using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=CGSzvzi6W5w 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Test list with 5 even numbers (2,4,8,20,6) and 4 odd numbers (5,11,13,15)
numbers_list = [2,5,4,8,11,13,15,20,6] 

# Program works by keeping a running count of the number of even numbers and 
# odd numbers found in the variables even_count and odd_count.  An even number
# has a remainder of 0 when divided by 1, an odd number has a remainder of 1
# when divided by 2.  So we have a for loop iterate over each number in the list
# where with each loop iteration 'number' will be set to the next number in 
# the list.  We then divide the number by 2 using the modulus operator % which
# provides the remainder of a division operation. And in the if branch we 
# check to see if the remainder is 0 which would tell us we have an even number
# and we increment even_count to acknowledge we have found another even number,
# and if this is not the case then in the elif branch we check to see if 
# dividing the number by 2 gives us a remainder of 1 which would tell us we have
# an odd number and we increment odd_count to acknowledge that we have found 
# another odd number.  By the time the loop is done we will have counted all 
# the even and odd numbers in the list.
#
even_count = 0
odd_count = 0
for number in numbers_list:
    if number % 2 == 0:
        even_count += 1
    elif number % 2 == 1:
        odd_count += 1

# Output the results
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
