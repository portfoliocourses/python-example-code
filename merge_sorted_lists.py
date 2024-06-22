################################################################################
#
# Program: Merge Two Sorted Lists
#  
# Description: Program to merge two sorted lists using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=p3fBGZk_ctM
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns a new list containing the items of the sorted lists list1 and list2 
# merged together in sorted order.  The function utilizes the fact that these
# two lists are already sorted to perform this operation more efficiently.
def merge_sorted_lists(list1, list2):
    
    # A new merged list will be built from scratch
    merged = []

    # We'll go through the items in the sorted lists one at a time using a loop 
    # to build the merged list.  We'll use counter variable i to keep track of 
    # our position in list1, and counter variable j to keep track of our 
    # position in list2.  We also find the length of each list so we can 
    # recognize when we reach the end of a list.
    #
    i, j = 0, 0 
    len1, len2 = len(list1), len(list2)
    
    # Because list1 and list2 are sorted, i and j will begin by storing the 
    # index of the smallest item in each list, and as we increment i and j
    # they will store the index of the NEXT smallest item in each list.  The 
    # index that i and j store are the indexes of the "next smallest item" 
    # in each list.  We go through the lists using i and j and each time we
    # find the next smallest item in EITHER list and appending that item to
    # the merged list (and then incremented the counter variable for the list
    # from which the item was taken so that it now stores the index of the
    # NEXT smallest item in that list).  Eventually we will reach the end 
    # of one of these lists when i == len1 and or j == len2, at which point
    # we can stop.
    #
    while i < len1 and j < len2:
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    # To finish the merged list we can just concatenate the remaining items
    # from the other list which we did not reach the end of yet to the merged 
    # list.  Because i and j keep track of "how far we made it" into each list
    # we use the list slicing operator to (e.g. list1[i:]) to get a list made
    # up of the remaining items from the index i on in list1 and from the index 
    # j on in list2.  We then concatenate these to the merged list.  Keep in 
    # mind that because either i == len1 or j == len2, in one of these cases 
    # the slicing operation is going to return an empty list as there are no 
    # more items remaining in the list from that index onwards.
    # 
    return merged + list1[i:] + list2[j:]


# Test case sorted lists
l1 = [1,3,5,7,9]
l2 = [2,4,6,8,10]

# Test the function and output the resulting merged list
merged = merge_sorted_lists(l1,l2)
print(merged)