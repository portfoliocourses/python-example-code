################################################################################
#
# Program: Print A 1D Multiplication Table
#
# Description: A program to print a 1D multiplication table using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=ZO5tsBSbdn4 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# This program outputs "1D" multiplication tables like the one below, where a 
# number (in this case 5) is multiplied by all integers from 1 to some limit 
# (in this case 10).
#
#  5 x 1 = 5
#  5 x 2 = 10
#  5 x 3 = 15
#  5 x 4 = 20
#  5 x 5 = 25
#  5 x 6 = 30
#  5 x 7 = 35
#  5 x 8 = 40
#  5 x 9 = 45
#  5 x 10 = 50
  
# Prompt the user to enter the number and limit.  We convert the string that 
# input() returns to an int and store the int values into number and limit.
number = int(input("Number: "))
limit = int(input("Limit: "))

# We can't really create a multiplication table if the limit is less than or 
# equal to 0, so in this case we output an error message
if limit <= 0:
    print("Limit must be greater than 0")
# Otherwise we output the multiplication table
else:
    # This for loop will execute for i=1,2,...limit with each loop iteration,
    # and output number x i = number*i with each iteration to build the table
    for i in range(1, limit+1):
        print(number, "x", i, "=", number * i)
