################################################################################
#
# Program: Tuple Examples
# 
# Description: Examples of using tuples in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=33NPCB7zn7Q 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Tuples store a fixed number of items in an ordered way (at indexes 0,1,2...)
# and can contain duplicate values.


# Create a tuple containing 3 string items...
#
# Index: 0        1         2             3
shapes = ("circle", "rectangle", "circle")

# Output the tuple
print(shapes)

# The index operator [] can be used to access tuple items, here we access the
# 2nd item in the tuple
print(shapes[1])

# Tuples immutable, so we cannot add items to a tuple, or remove items from a 
# tuple, or alter which items a tuple stores.  The below statement will cause
# an error to occur.
#
# shapes[1] = "square"


# The len() function will return the number of items in the tuple, i.e. the 
# tuple length.
print("length:", len(shapes))


# The in operator can be used to check if a value is in a tuple
if "circle" in shapes:
    print("circle is in shapes")

# The not in operator can be used to check if a value is not in a tuple
if "apple" not in shapes:
    print("apple is not in shapes")


# We can loop through the tuple items with a for loop, in this loop with each 
# loop iteration 'shape' will be set to the next item in the tuple, from the 
# first item in the tuple to the last item, and we output that item each time.
for shape in shapes:
    print(shape)


# We could loop through the indexes of the tuple, range(len(shapes)) will have
# i be set to 0,1,2...len(shapes)-1 with each loop iteration.  We could use 
# i to access the tuple items if we like, as we do here to output each tuple
# item in the loop body.
for i in range(len(shapes)):
    print(shapes[i])


# A tuple can store different types of values, as the below example stores a 
# string, an int, a bool, and a float.
mixed = ("string", False, 2, 5.6)

# Output the tuple containing a mixture of different types of values
print(mixed)


# We can create tuples with a single item if we put a comma after the item
one_item = ("item", )

# Output the type of one_item to verify it is a tuple
print(type(one_item))


# Brackets are only needed when creating tuples if not using brackets would 
# be ambiguous.  Below we create a tuple without using brackets.
multiple = 1,2,3,4

# Output the tuple
print("multiple:", multiple)


# We can create an empty tuple containing no items, to do so we need to use 
# brackets to create the tuple.
empty = ()

# Output the empty tuple
print("empty:", empty)


# We sometimes want to 'unpack' tuples and store the items of the tuple into 
# different variables.  Here we create a test tuple with 3 strings.
names = ("Jim", "Dwight", "Pam")

# We can then 'unpack' the items of the tuple, storing each tuple item into 
# the variables person1, person2 and person3
person1, person2, person3 = names 

# Output the variables to verify that person1 will store "Jim", person2 will
# store "Dwight", and person3 will store "Pam"
print("person1:", person1)
print("person2:", person2)
print("person3:", person3)


# We can unpack some number of items into a list using the * operator, we'll
# test this using this numbers tuple.
numbers = (1,2,3,4,5)

# The first two tuple items 1 and 2 will be unpacked to n1 and n2, and then 
# due to the * operator the rest of the tuple items 3,4,5 will be unpacked 
# into a list [3,4,5] that rest will store.
n1, n2, *rest = numbers

# Output n1, n2 and rest to verify this behaviour
print("n1:", n1)
print("n2:", n2)
print("rest:", rest)

# We could put variables after the variable with the * operator, so here n3 
# will store 5 and rest will then store the list [3,4].
n1, n2, *rest, n3 = numbers 

# Output n1, n2, rest and n3 to verify this behaviour
print("n1:", n1)
print("n2:", n2)
print("rest:", rest)
print("n3:", n3)


# A common use case for tuple unpacking is creating functions which return
# more than one value... the below function technically only returns one 
# value, a tuple object.  But the tuple object stores 3 ints: 1,2,3.  And 
# so we are using the tuple to return 3 values.
def function():
    return 1,2,3

# When we call the function, we unpack the returned tuple into 3 variables.
(v1,v2,v3) = function()

# Output to confirm v1=1, v2=2 and v3=3
print("v1:", v1)
print("v2:", v2)
print("v3:", v3)


# We can join tuples together using the + operator, we'll create two tuples to 
# test this...
first = (1,2)
second = (3,4)

# The + operator will create a new tuple with the items (1,2,3,4) from joining 
# together the tuples first and second.
joined = first + second 

# Output the joined tuple to confirm the expected tuple is (1,2,3,4)
print("joined:", joined)


# We can also use the multiply operator * to 'multiply' a tuple, below we'll 
# create a new tuple that is essentially the first tuple joined 3x together. 
multi = first * 3

# Output the tuple to confirm the expected tuple is (1,2,1,2,1,2)
print("multi:", multi)


# Tuples have a count method that allow us to count the occurrences of a value
# in the tuple, here we count the occurrences of the value '1' in the multi 
# tuple above (i.e. 3).
print("one count:", multi.count(1))


# We can use the index method to find the first index in the tuple where a 
# value occurs.  Let's create a basic tuple to test this method.
#
# index:   0   1   2   3
results = (12, 45, 34, 56)

# The index() method wil return 2 in the case of 34
print("index:", results.index(34))

# The index() method raises an exception if the value is not found, for example
# 55 is not in the results tuple and the below statement will cause an exception
# if we uncomment it.
#
# print("index:", results.index(55))


# We can use the tuple() function to construct a tuple from iterable objects 
# like lists and ranges.  This will create a tuple with the items 1,2,3
new_tuple = tuple([1,2,3])

# Output new_tuple to verify we have created a new tuple (1,2,3)
print(new_tuple)


# Tuples are immutable, which means we can't change which objects a tuple 
# stores.  A workaround for this is to convert a tuple to a list, modify the 
# desired index, and then convert the list back to a tuple.  Let's do that here.

# Create a test tuple
values = (1,2,3,4)

# Convert the tuple to a list
temp_list = list(values)

# Modify the 2nd item in the list, corresponding to the 2nd item in the original
# tuple at the index 1
temp_list[1] = 500

# Convert the list back to a tuple
values = tuple(temp_list)

# Output the tuple.  Notably this is a *new* tuple, we created a new list from 
# the original tuple, then we created a new tuple from this list.
print(values)


# We can use negative index and slicing syntax with tuples.  Let's create a test
# tuple storing letter strings...
#
# index:    0    1    2    3    4    5
letters = ("a", "b", "c", "d", "e", "f")

# The index "negative 2" (-2) will give us the 2nd last item in the list.
print(letters[-2])

# The slicing syntax 1:4 will give us a tuple with the items from index 1 in 
# this tuple up until but not including the item at index 4.  i.e. we'll get
# the tuple ("b", "c", "d") 
print(letters[1:4])

# If we omit the end index, we'll get the tuple containing the items from the
# start index up until the end of the original tuple... i.e. we'll get the 
# tuple ("b", "c", "d", "e", "f")
print(letters[1:])

# If we omit the start index, we'll get the tuple containing the items from the
# first index up until but not including the end index... i.e. we'll get the 
# tuple ("a", "b", "c", "d")
print(letters[:4])


# We can delete a tuple with the delete statement.
del letters 

# This will delete the tuple and if we try to output letters we'll get an error.
# print(letters)


# Notably even though tuples are immutable, if they store mutable objects such
# as lists, we can still modify the internal state of these mutable objects.

# Create a simple tuple which stores a mutable list object as its first item
simple_tuple = ([1], 2, 3)

# Append 55 to the list stored at the first index
simple_tuple[0].append(55)

# Output the tuple... the tuple stores the same objects as before because it is
# immutable, but the list stored at the first index is mutable, and we were able
# to append 55 to this list.
print(simple_tuple)