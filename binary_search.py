################################################################################
#
# Program: Binary Search Algorithm
# 
# Description: A recursive implementation of the binary search algorithm in 
# Python.  See the binary search algorithm article on Wikipedia for more
# information: https://en.wikipedia.org/wiki/Binary_search_algorithm.
#
# YouTube Lesson: https://www.youtube.com/watch?v=eBcMm_V1LLA 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# We implement a recursive version of the algorithm that calls itself at each 
# step with new low and high indexes that restrict the algorithm's search to an 
# increasingly small portion of the list.  The function is passed the list and 
# the element to find in the list as arguments, as well as 'low' and 'high' 
# which identify the range of indexes in which the algorithm is currently 
# searching for the element.  Initially low and high should be the entire 
# range of indexes in the list, if we are attempting to find the element in 
# the entire list.
#
# The algorithm works by repeatedly finding the middle index between low and 
# high.  If the element is found at this index, we have found the element and 
# return the index.  If the element is greater than the element found at this 
# middle index, the element must be in the right-half of the current portion of 
# the list we are looking at, and we apply the algorithm to this right half 
# by making mid+1 'the new low' when we call the function again.  In the same 
# way if the element is less than the element found at this middle index, the 
# element must be in the left-half of the current portion of the list we are 
# looking at, and we apply the algorithm to this left half by making mid-1 'the
# new high' when we call the function again.  If we ever call the function with 
# a low index that is greater than or equal to the high index, then the element
# is not in the list at all and we can return None to represent this.
# 
def binary_search(list,elem,low,high):
  if (low >= high):
    return None
  else:
    mid = low + (high-low) // 2
    if (elem == list[mid]):
      return mid 
    elif (elem > list[mid]):
      return binary_search(list,elem,mid+1,high)
    else:
      return binary_search(list,elem,low,mid-1)

# The binary search algorithm works on sorted lists like this one
slist = [1,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# We pass the list, the element to find '15', and the initial low and high 
# indexes as 0 and len(slist)-1, i.e. the entire list. The high index is the 
# last index in the list, we need to subtract 1 from the length of the list 
# to get this index as lists in Python are zero-indexed.
result1 = binary_search(slist,15,0,len(slist)-1)

# We should get index '13' as the index of element 15
print(result1)

# If we try to find element '2' we should get back None as it is not in the list
result2 = binary_search(slist,2,0,len(slist)-1)
print(result2)