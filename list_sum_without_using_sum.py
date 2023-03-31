################################################################################
#
# Program: Find Sum Of Numbers In A List Without Using sum()
# 
# Description: Calculate the sum of the numbers in a list in Python without 
# using the built-in sum() function.
#
# YouTube Lesson: https://www.youtube.com/watch?v=xoupTp2sx48 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Test list with a sum of 55
list = [1,2,3,4,5,6,7,8,9,10]

# The built in sum() function will return the sum of the numbers in the list
list_sum = sum(list)

# Output the returned value to confirm the list sum is 55
print("list_sum:", list_sum)

# We can calculate the sum of the numbers in the list by adding each number in 
# the list to a variable initially set to 0.  Here we set manual_sum to 0, and 
# then loop through each number in the list, adding it to manual_sum.
manual_sum = 0
for number in list:
  manual_sum += number 

# Output the manual_sum to confirm it is also 55
print("manual_sum:", manual_sum)

# We can create a function to perform this algorithm, here we loop through the 
# elements of the parameter list_to_sum to find the sum, which we return from 
# the function.
def _sum(list_to_sum):
  sum_of_list = 0
  for number in list_to_sum:
    sum_of_list += number 
  return sum_of_list 

# Call our own _sum() function to calculate the list sum
function_sum = _sum(list)

# Output function_sum to confirm the list sum is 55
print("function_sum:", function_sum)