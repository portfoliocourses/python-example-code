################################################################################
#
# Program: List Basics
# 
# Description: Examples covering the basics of lists in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=k7cVsK5wXTU 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Creates a list with 3 items, a is a reference to the list.  Lists are a 
# built-in type in Python which allow us to store an ordered collection of data.
# The items are available at an index, starting from 0...
#
#    0  1 2    <- indexes
a = [2,-4,6]

# Output the entire list
print(a)

# Access the item at the index 0, the first item in the list, and output it
print(a[0])

# Output the item at index 2, the third item in the list
print(a[2])

# We can modify the items in a list, here was modify the 2nd item to be 100. We
# output the list so we can see the modified value.  
a[1] = 100 
print(a)

# The append method will append a new item to the end of the list, here we 
# append 7 to the end of list.
a.append(7)
print(a)

# The insert method will insert a new item at an index, here we insert the value
# 3 at the index 1, the items at index 1 and beyond will be shifted down by 1
# index.
a.insert(1,3)
print(a)

# The extend method will append a list to the list... in this case the items 8
# and 4 will be appended to the end of the list.
a.extend([8,4])
print(a)

# We can del to remove an item from the list, here we remove the 2nd item in 
# the list (at the index 1).  The remaining items past index 1 will be shifted
# down as a result.
del a[1]
print(a)

# The remove method will remove the first occurrence of a value in the list, 
# so here we remove the first occurrence of the value 8 from the list.
a.remove(8)
print(a)

# The pop method when it is passed no arguments will remove and return the 
# last item in the list.
last = a.pop()
print(a)
print(last)

# The pop method when it is passed an index as an argument will remove and 
# return the item at that index.
third = a.pop(2)
print(a)
print(third)

# The len() function will return the length of the list (i.e. the number of 
# items in the list).
print("length:", len(a))

# The in operator can be used to check if a value is in the list, here we 
# check if the value 100 is in the list a.  The result will be True if it is,
# and False otherwise.
if 100 in a:
    print("100 is in list")
else:
    print("100 is not in list")

# The reverse method will reverse the order of the items in the list.
a.reverse()
print(a)

# The sort method will sort the list items in ascending order.
a.sort()
print(a)

# If we pass the sort method reverse = True the items will be sorted in 
# descending order.
a.sort(reverse = True)
print(a)

# Lists can store all types of data, for example this list stores strings.
string_list = ["Luke", "Han", "Leia"]
print(string_list)

# The sort method will sort a list of strings alphabetically
string_list.sort()
print(string_list)

# Lists in Python support storing multiple different types of data in the same
# list... here we have a list that stores an integer value, a boolean value, a
# string value, and even another list value!
mixed_list = [2, True, "X", [1,2]]
print(mixed_list)

# The assignment operator does NOT create a new list.  So here when we create a
# new list and have x reference that list, and then assign x to y, a copy of the
# list is NOT created.
x = [1,2,3]
y = x 

#  Instead both x and y will reference the SAME list.
#
#        [1,2,3]
#       /      \
#      x        y

# So if we modify the list that y references at the index 1, it will ALSO modify
# the list that x references because they are the SAME list.
y[1] = 100

#  After...
#
#        [1,100,3]
#       /      \
#      x        y

# If we output x and y we'll find we get [1,100,3] in both cases because they 
# both reference the SAME modified list.
print("x:", x)
print("y:", y)

# To create an actual copy of the list we can use the copy method... here w 
# will reference a new copy of the list that q references
q = [1,2,3]
w = q.copy()

#  So q and w reference DIFFERENT lists and when we alter the list that w 
#  references below it will not effect the list that q references. 
#
#    [1,2,3]      [1,100,3]
#   /            /
#  q            w

w[1] = 100

# Now if we output q and w we'll get two different lists... [1,2,3] for q and
# [1,100,3] for w...
print("q:", q)
print("w:", w)

# Here we create a list of strings to test the slicing operator...
#
#           0    1    2    3    4    5    <- indexes
letters = ["a", "b", "c", "d", "e", "f"]

# The slicing operator allows us to create a new list made up of some portion
# of items in the original list... here we'll get a new list made up of the 
# items FROM the index 1 up until but not including the index 4.
letters_slice = letters[1:4]
print(letters_slice)

# We can use a for loop to loop through the items in a list.  The for loop
# body will run for each item in the list in order, and letter will be set to 
# each item as the loop body executes.
for letter in letters:
    print(letter)

# The clear method will remove all the items in a list, giving us an empty list.
letters.clear()
print(letters)

# Create two test lists to test the concatenation operator +
list1 = [1,2,3]
list2 = [4,5,6]

# The + concatenation operator will give us a new list made by concatenating 
# the lists list1 and list2, so we'll get the list with the items of list1 
# followed by the items of list2.
new_list = list1 + list2 
print(new_list)
