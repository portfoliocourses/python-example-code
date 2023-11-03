################################################################################
#
# Program: Bubble Sort
# 
# Description: An implementation of the Bubble Sort algorithm in Python. See the
# wikipedia article on Bubble Sort: https://en.wikipedia.org/wiki/Bubble_sort
#
# YouTube Lesson: https://www.youtube.com/watch?v=SqUpPwiTSak 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Sorts the list 'a' using the bubble sort algorithm
def bubble_sort(a):

    # Find the length of the list 
    length = len(a)

    # Perform up to length-1 number of "passes" through the list
    for i in range(0,length-1):

        # We can perform less passes if the list happens to be sorted with 
        # a fewer number of passes. We'll use swapped to help us detect 
        # whether a swap occurred.  If no swap occurs during a pass, the list
        # must already be sorted.
        swapped = False

        # Make a "pass" through the list, compare the item at each index to
        # the item in the adjacent index, and swap them if they are not 
        # in ascending order.  We set swapped to True if a swap occurs, which
        # tells us the list was not yet sorted at the beginning of this pass.
        # We initially have the counter variable go from 0,length-2, the 
        # 2nd last index of the list. This is because the last item in the
        # list has no item at j+1. With each pass through the list the
        # next largest item in the list will have been shifted down to 
        # its correct position in the sorted list. i.e. after the first pass
        # through the list the largest item will be in the last index of 
        # the list, after the second pass through the list the second 
        # largest item will be in the second last index of the list, and
        # so on.  We don't need to perform any comparisons with the these 
        # last items because we already know they are in the correct positino.
        # So we have length - i - 1, subtracting i, for the end of the 
        # range, so that we go one less item deep into the list each time
        # with each pass as i goes from 0,1,2,... and on in the outer loop.
        for j in range(0,length-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True 

        # If no swap occurs, we have discovered the list is now sorted and 
        # break to stop the outer loop early as no more passes are required.
        if not swapped:
            break

# A test list for bubble sort to sort
a = [6,5,3,1,8,7,2,4]

# Call the function to sort 'a'
bubble_sort(a)

# Output the now sorted list
print(a) 