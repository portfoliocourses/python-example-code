################################################################################
#
# Program: Loop Through A List Using A While Loop
#  
# Description: Program to loop through a list using a while loop in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=5oI5qWwn_xE 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# An example list with 5 items of length 5
data = [5,6,7,8,9]

# We could use a for loop to loop through the items of the list (also called 
# iterating over the items of the list).  The for loop body will run for each
# item in the list in order, and each time it does item will be set to the next
# item in the list.
for item in data:
    print(data)

# We could instead use a while loop to loop over the items in the list.  A 
# while loop will run as long as some condition is true. Each item in the list 
# 'data' is available at an index:
#
#         ->i->
#         0 1 2 3 4   <- indexes
# data = [5,6,7,8,9]
# 
# We can begin a special variable 'i' called a "counter variable" off at the 
# index 0 before the first loop iteration.  We can then use 'i' to access the 
# items of the list with data[i], so in the first loop iteration we access 
# the first item in the list at the index 0.  At the end of the loop body we 
# can increment i by 1 using i += 1.  In this way, with each loop iteration 
# i will move in-order through the indexes of the list from 0 to 1 to 2 and 
# so on.  
#
# The length of the list is 5 which we can find by calling len() and passing 
# it the list.  We have the loop condition 'i < len(data)' to continue the 
# loop so long as i < 5, i.e. we continue the loop so long as i has not yet
# reached the length of the list as the last item in the list will be 
# accessible at the index len(data) - 1 == 4.
#
i = 0
while i < len(data):
    print(data[i])
    i += 1

# While it's generally preferable to use a for loop to loop through the items
# in a list, a while loop and counter variable can be very flexible.  For 
# example here we "skip over" the next item in the list if the item at 
# the current index i is equal to 6, by incrementing the counter variable 'i'
# by 2 in this case (but by 1 otherwise).
#
i = 0
while i < len(data):
    print(data[i])
    if data[i] == 6:
        i += 2
    else:
        i += 1