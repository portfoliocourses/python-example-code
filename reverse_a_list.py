################################################################################
#
# Program: Reverse A List Without Using reverse()
# 
# Description: An example of how to reverse a list in Python without using the
# built-in .reverse() method.
#
# YouTube Lesson: https://www.youtube.com/watch?v=byxdI22yt_E
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A list of numbers for test purposes
numbers = [5,6,7,8,9]

# We could call the built-in reverse() method to reverse the list
# numbers.reverse()

# There are many ways to "manually" reverse a list.  The below loop will 
# continually remove the last item in the list and insert it into the 
# list at the next index in the list going from 0,1,2,... up until (but not
# including) the last index in the list because that item will be in its
# correct position at that point.  The loop will run with i set to the 
# indexes 0,1,2,...len(numbers)-2, and we use this index to perform the
# insert.  We use the built-in .insert() method to insert the item and 
# the .pop() method which removes and returns the last item in the list.
for i in range(len(numbers) - 1):
    numbers.insert(i, numbers.pop())
    
    # We could output i and the numbers list to see how the algorithm works
    # print(i, numbers)

# We could also use the slicing operator to reverse a list, this application 
# of the operator will create a new list made up of the items of numbers 
# going from the last item in the list to the first item in the list and 
# including each item in that order in the new list.  We store the resulting
# new list back into numbers so that numbers now stores (references) the
# reversed list.
numbers = numbers[::-1]

# Output the now reversed list
print(numbers)