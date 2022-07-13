################################################################################
#
# Program: Insertion Sort
# 
# Description: An implementation of the insertion sort algorithm in Python.  See
# a description of the algorithm: https://en.wikipedia.org/wiki/Insertion_sort
#
# YouTube Lesson: https://www.youtube.com/watch?v=E-_lIK5we84 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Sorts the list using the insertion sort algorithm
def insertion_sort(list):
  
  # Initially the first element in the list is considered to be 'sorted' as 
  # one element is sorted by default.  The outer loop will continually set the 
  # next element in the unsorted portion of the list as the next key, and the 
  # inner loop will move that key into its correct position in the sorted 
  # portion of the list.  The unsorted portion of the list will thus become 
  # one element smaller with each iteration of the outer loop.  We have a 
  # range from 1 to the length of the list because we 'skip over' that first 
  # element at index 0 because this is our initial sorted portion of the list.
  for i in range(1,len(list)):
    
    # Set the key to be the next element in the unsorted portion of the list 
    # as identified by index i.
    key = list[i]
    
    # The inner loop will shift the key into its correct position in the 
    # sorted portion of the list (which could be at the very beginning of the 
    # list if it is smaller than all elements in the sorted portion of the 
    # list).  We do this by examining each element in the sorted portion of
    # the list from right to left, with 'j' being used to keep track of the 
    # current element we are examining.  We initialize j to i - 1 because 
    # this will give us the element one to the right of the key, the rightmost
    # element in the sorted portion of the list.
    j = i - 1

    # We keep moving over the element we are currently looking at, at index j, 
    # to the list index one to the right (j + 1), so long as the key is less 
    # than the element we are currently looking at (key < list[j]) and we 
    # not yet reached the beginning of the list (j >= 0).
    while j >= 0 and key < list[j]:
      list[j + 1] = list[j]
      j -= 1
    
    # After the above loop, we'll have either found the index where the key 
    # is no longer smaller than an element in the sorted portion, or we've 
    # reached the start of the list.  Either way, this is where the key 
    # value needs to be placed so we store it here.
    list[j + 1] = key 


# a test list to sort
test_list = [9,5,8,3,4,7]

# call the insertion sort function to sort the test list
insertion_sort(test_list)

# output the test list after it has been sorted
print(test_list)




#   The below is a description/illustration of 
#   the insertion sort algorithm that was 
#   covered in the YouTube video tutorial for
#   this code...
#
#
#
#   Insertion Sort works by continually sliding
#   over the next element ("the key") in the 
#   unsorted portion of the list to its correct
#   position in the sorted portion of the list.
# 
#    
#   Example... 
#
#   Sorted Portion  Unsorted Portion
#       |        |  |        |
#       3, 5, 7, 8, 6, 2, 9, 4
#                   |
#                  Key
#
# 
#   6 belongs between 5 and 7 in the sorted 
#   portion of the the list...
#
#       3, 5, 6, 7, 8, 2, 9, 4
#             |
#            key
#
#
#   In order to move the key to the correct 
#   position, we examine each element from 
#   right to left in the sorted portion, and
#   shift the element to the right if it is 
#   smaller than the key.
#
#
#    key = 6
# 
#                |   
#       3, 5, 7, 8, 6, 2, 9, 4 
#                |
#       6 < 8 so shift 8 over
#                |  
#       3, 5, 7, 8, 8, 2, 9, 4 
#                   |
#                   8 is shifted over
# 
#
#    key = 6
#               
#             |    
#       3, 5, 7, 8, 8, 2, 9, 4 
#             |
#       6 < 7 so shift 7 over
#             |
#       3, 5, 7, 7, 8, 2, 9, 4 
#                |
#                7 is shifted over
#
#
#    key = 6
#   
#          |
#       3, 5, 7, 7, 8, 2, 9, 4 
#          |
#       6 > 5 so we've found where 6 belongs!
#          |  
#       3, 5, 6, 7, 8, 2, 9, 4 
#             |
#             Insert 6 here
#
#
#   If a key slides right to the beginning
#   of the list, we stop at that point too.
#
#   This process of sliding over the next key 
#   happens until the entire list is sorted. 
#
#   We start off with the first element of the 
#   list as the "sorted portion".      