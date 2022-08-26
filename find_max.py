################################################################################
#
# Program: Find The Maximum Number In A List WITHOUT Using max().
# 
# Description: How to find the largest value in a list in Python without using 
# the built-in max() function.
#
# YouTube Lesson: https://www.youtube.com/watch?v=RNHhgJcDjI8 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns the maximum value in the list supplied as an argument
def find_max(list):
  
  # Assume that the first element in the list is the maximum value in the list
  max = list[0]
  
  # Go through the remaining elements in the list, and whenever a value is 
  # encountered that is greater than the current max value, make this value 
  # the new max value.
  for number in list:
    if (number > max):
      max = number 
  
  # By the end of the above loop max will contain the largest value in the 
  # list and we return that value from the function
  return max

# An example list where 9 is the max value
list = [3,7,5,8,4,9]

# Call the find_max() function with the list as an argument, store the max value
# returned into max
max = find_max(list)

# Print out the max value that was found in the list
print("Max:", max)



# Python's built-in max() function will also find the maximum value...
#
# print(max(list))



# We don't need to put the algorithm to find the maximum number in a list inside
# a function, we could just write a simple program like this instead:
#
#
# list = [3,7,5,8,4,9]
#
#  max = list[0]
#  for data in list:
#    if (data > max):
#      max = data
#
# print("Max:", max)