################################################################################
#
# Program: Mutable vs Immutable Objects
# 
# Description: Examples illustrating the difference between mutable and 
# immutable objects in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=GzMvimgJIDM 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Objects in Python are either mutable or immutable.
#
# We can change the 'internal data' of mutable objects, we cannot change the 
# 'internal data' of immutable objects.
#
# Types like lists, dictionaries and sets are mutable.
#
# Types like strings, numbers (ints, floats, etc), tuples and frozen sets are
# immutable.
#
# User-defined classes are immutable, but this is ultimately up to the 
# definition of the class.


# x is a variable that references an object of type Int that represents the 
# integer value 4
x = 4

# Every object in Python has a unique integer id which is typically the memory 
# address of the object (though this technically depends on the implementation 
# of Python).  The id() function will return this id, i.e. the id of the object
# that x references.
print("id(x):", id(x))

# When we assign x to y, a copy of the object x references is NOT created, 
# instead y will reference the same object that x references.
y = x

# If we call id(y) we'll get the same id as id(X) because both x and y reference
# the same object.
print("id(y)", id(y))

# Int objects are immutable, so x + 2 will actually result in the creation of a 
# NEW Int object (6) that x will then reference.
x = x + 2

# We'll see that x is now 6...
print("x:", x)

# id(x) will now return a DIFFERENT idea than the last call to id(x) because x 
# references a different object
print("id(x):", id(x))

# id(y) still references the Int object for 4 as before
print("id(y):", id(y))


# Strings are also immutable objects, here test references the string 
# object "abc"
test = "abc"

# Output the id of the object test references
print("id(test):", id(test))

# Concatenating test with "123" will produce a new string object "abc123" that 
# test will then be assigned to reference
test = test + "123"

# We'll see that test is now "abc123"
print(test)

# But id of the object that test references will be different because test now
# references a DIFFERENT/NEW string object, because the existing string was not 
# modified because strings are immutable, instead a new string object was 
# created altogether.
print("id(test):", id(test))


# Lists are mutable, here we create a list [1,2,3] numbers will reference it
numbers = [1,2,3]

# Output the id of the list object that numbers references
print("id(numbers):", id(numbers))

# Because lists are mutable, we can actually change their "internal state", here
# we append 4 to the list.  But this will NOT change which list objects numbers
# references, instead we've changed the "internal state" of the object that 
# numbers references.
numbers.append(4)

# numbers will now be the list [1,2,3,4]
print(numbers)

# The id of the list object that numbers references will be the same as before
print("id(numbers):", id(numbers))


# Technically that list doesn't store the "values" 1,2,3,4, technically what it 
# stores is references to Int objects 1,2,3,4.  This can sometimes make the 
# distinction between mutable and immutable types confusing.  So for example 
# tuples are immutable, but what that means is that we can't change WHICH 
# objects a tuple references.  Whatever a tuple references, it will continue
# to reference. But we CAN change the "internal state" of mutable objects that
# the tuple references.


# tuple_with_list will reference this tuple object, the first item is a list 
# object that the tuple references, and lists are mutable.
tuple_with_list = ([1], 5, 6)

# Output the tuple
print(tuple_with_list)

# Output the id of the tuple object that tuple_with_list references
print(id(tuple_with_list))

# We can modify the list object that the first index of the tuple references,
# we are not changing the tuple's internal state when we do this.  The tuple 
# will stay reference that same list object as before.  What we're changing is
# the internal state of the mutable list object that the tuple references.
tuple_with_list[0].append(2)

# The tuple's first item will now be the list [1,2]
print(tuple_with_list)

# The id of the tuple object that tuple_with_list references will not change
print(id(tuple_with_list))


# Mutable vs immutable objects has important implications for passing arguments
# to functions.  Python has what is called pass by assignment.  When we pass an 
# argument to a function, whatever object the argument is referencing will 
# become what the parameter variable is referencing.  Note that this is not the 
# same thing as pass by reference, it's more accurately "passing a reference 
# by value".  

#  This add function adds 1 to m
def add(m):

    # Initially the id of the object m references will be the same as y below
    print("id(m):", id(m))

    # If we add 1 to m and assign the result to m a new Int object will be 
    # created and m will reference this object
    m = m + 1

    # If we output the id of the object that m references, it will now change, 
    # it will be a new object.
    print("id(m):", id(m))

    # return the new value so we can assign it back to y, as the function will
    # NOT modify y below unless we return this value and assign it to y as 
    # adding 1 to m created a new Int object altogether
    return m
   
# y will reference an Int object 5
y = 5

# If we output the id of the object that y references, we'll see it matches what
# the parameter m is initially set to in the function above.  That's because the
# reference is what was really passed to the function, as if we had done: m = y
print("id(y)", id(y))

# If we call add and pass it y, the statement m = m + 1 will NOT add 1 to y, 
# instead a new Int object is created.  But we have the function return the new
# value/reference after adding m + 1 and we assign it to y to modify y by 
# calling the function.
y = add(y)

# y will now be 6
print("y:", y)

# y will now reference the same new Int object that was created in the function
print("id(y)", id(y))


# If we pass a mutable type like a list to a function, the function can change 
# the list without returning a new list.  Here we append the string "X" to the 
# list letters, but if we output the id of the object that letters references 
# we'll find it's the exact same as the object uppercase below references even
# AFTER modifying the list... and this is because lists are mutable, we CAN 
# change their internal state!
def add_to_list(letters):
    letters.append("X")
    print("id(letters)", id(letters))

# uppercase references the list with the items "A", "B" and "C"   
uppercase = ["A", "B", "C"]

# Output the id of the list object that uppercase references, we'll find it's
# the same as the letters variable in the function above.
print("id(uppercase):", id(uppercase))

# Call add_to_list, it will append "X" to the list object that uppercase 
# references
add_to_list(uppercase)

# If we output the list we'll see it's now ["A", "B", "C", "X"]
print("uppercase:", uppercase)

# The above example behaves a lot like a concept called "pass by reference" in 
# other languages.  But the parameter letters is not using "pass by reference".
# Instead we have pass by assignment, as if we had done:
#
# letters = uppercase
#
# and now letters references the same object that uppercase references.  But 
# letters is a variable like others that could be set to reference another 
# object like this:
#
# letters = ["X", "Y", "Z"]
#
# and if we did, this would have no effect on uppercase or the list that it is 
# referencing it... instead letters would reference a whole new list.