################################################################################
#
# Program: Remove Negative Numbers From A List
# 
# Description: Remove negative numbers from a list in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=OD3Tg9VOJfM 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################


nums = [4,-5,6,8,-3,6,9,-4]

# Approach #1 - Create a new list made up of only elements from nums that 
# are non-negative.
#
# for item in my_list:
#  if (item >= 0):
#    filtered_list.append(item)
#
# print(filtered)


# Approach #2 - Use the filter function with check_number function as an 
# argument to create a new list with only non-negative numbers.
#
# def check_number(number):
#  return number >= 0
#
# filtered = list(filter(check_number, nums))
#
# print(filtered)


# Approach #3 - Use the filter function, but use a lambda function (anonymous 
# function) instead.
#
# def check_number(number):
#  return number >= 0
#
# filtered = list(filter(lambda n : n >= 0, nums))
#
# print(filtered)


# Approach #4 - Use a list comprehension to create a new list from the old 
# list that only contains non-negative numbers
#

filtered = [item for item in nums if item >= 0]

print(filtered)