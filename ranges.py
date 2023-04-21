################################################################################
#
# Program: Using Ranges With range()
# 
# Description: Examples of using Ranges with range() in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=Vsv1c-OKPB4  
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Ranges represent immutable sequences of numbers based on start, stop and 
# step values.  If the step value is positive the sequence is given by the 
# formula:
#
# r[i] = start + (step * i)
#
# where i >= 0 and r[i] < stop
#
# We create range objects using the range constructor functions.


# A range with a start value of 0, a stop value of 5, and a step value of 1. 
# A range only stores the start, stop and step values, generating the numbers
# in the range/sequence as needed.  We convert the range to a list using list()
# before outputting the list so we can see all the numbers in the sequence.  
# This range results in the sequence of numbers: 0 1 2 3 4
print(list(range(0,5,1)))


# The below range will give us the sequence: 2 4 6 8 10 12.  The arguments to 
# range need to be integers, but it could be something that evaluates to an 
# integer such as "x + 1" which evaluates to 2.
x = 1
print(list(range(2,13,x + 1)))


# If the step value is negative the sequence is defined using the formula...
#
# r[i] = start + (step * i)
#
# where i >= 0 and r[i] > stop 
#
# So the below range results in the sequence: 3 1 -1 -3 -5 -7
print(list(range(3,-8,-2)))


# If no step value is provided the step value defaults to 1 so the below range 
# will give us the sequence: 4 5 6 7 8
print(list(range(4,9)))


# There is another range constructor function which only accepts a single value
# as an argument, the stop value, with the start value defaulting to 0 and the
# step value defaulting to 1.  So this range gives us the sequence of numbers:
# 0 1 2 3 4 5
print(list(range(6)))


# It's possible to have a range with 0 numbers, here with a default step value 
# of 1, a start value of 0, and a stop value of -1, we have 0 numbers in the
# range as the stop value is less than the start value!  We will get the empty
# list when converting the range to a list.
print(list(range(0,-1)))


# Ranges are considered equal if they represent the same sequence of values,
# here range1 represents the sequence: 0 6
range1 = range(0,10,6)
print("range1:", list(range1))

# And even though it has a different stop value, range2 ALSO represents the 
# sequence: 0 6
range2 = range(0,11,6)
print("range2:", list(range2))

# So the equality operator will result in true because range1 and range2 are 
# considered equal!
if (range1 == range2):
    print("range1 equals range2")


# Representing a sequence of numbers with a list involves storing each number
# in the sequence as a list element
mylist = [2,4,6,8,10,12,14,16,18,20]

# But with a range we can represent a sequence by storing only the start, stop
# and step values, which is much more efficient, especially for large sequences.
myrange = range(2,22,2)

# If convert the range to a list and output it, we'll find it represents the 
# same sequence of numbers as the list above.
print(list(myrange))


# Range objects have start, stop and step members, e.g. myrange will have a 
# start value of 2, a stop value of 22, and a step value of 2.
print("myrange.start", myrange.start)
print("myrange.stop", myrange.stop)
print("myrange.step", myrange.step)


# Ranges are typically used to run a for loop body a certain number of times.
# Here range(10) will give us the sequence of numbers 0 1 2 3 4 5 6 7 8 9, 
# and so the for loop will run 10 times, and each time it does i will be set
# to the next number in the sequence.
print("Run a loop body 10x")
for i in range(10):
    print(i)

# We can use ranges with explicit start, stop and step values to have loop 
# counter variables go from a start value to a stop value by a step value, a 
# fairly common thing to do when creating loops made convenient by ranges.  
print("Counter from 3 to 20 by step 5")
for i in range(3,20,5):
    print(i)


# All common sequence operations are supported by ranges except concatenation 
# and repetition, as these operations could violate the pattern sequences are 
# required to follow:
#
# + - no concatenation
# * - no repetition 

# We can use the in operator to check if a value is in a range, here 1 is in 
# range(0,4) because range(0,4) is the sequence: 0 1 2 3
if (1 in range(0,4)):
    print("1 is in the range")

# We can use the not in operator, here to see that 10 is not in the range(0,4)
if (10 not in range(0,4)):
    print("10 is not in the range")

# We can use the len() length function to get the total number of numbers in the
# range/sequence, here we will get 4
print("len:", len(range(0,4)))

# We can use min() to get the minimum value in the range (here we will get 1)
print("min:", min(range(0,4)))

# We can use max() to get the maximum value in the range (here we will get 3)
print("max:", max(range(0,4)))

# We can use .count() to count the occurrences of a value in a range, here we 
# see that the value '1' occurs once in the range(0,10)
print( range(0,10).count(1) )

# We can use .index() to find the index of the first occurrence of a value in 
# a range, here we find that the first occurrence of the value 4 in the range 
# is at the index 2.
#
# value: 2 3 4 5
# index: 0 1 2 3
#
print( range(2,6).index(4) )

# We can use the index operator to get the value at an index in the range, so 
# here we get that the value 3 occurs at the range 1.
print( range(2,6)[1] ) 

# We can also use the slice operator to get a slice of the range, i.e. a new 
# range made up of some 'slice' or portion of the original range based on 
# start, stop and step values working with the range indexes.
#
# So the below range(0,20,2) will give us the following values at the following
# indexes, and the slice operator [2:10:3] has a start value of 2, a stop value
# of 10, and a step value of 3.  The slice operator works with the indexes of 
# the range, giving us a new range made up of the values at the indexes 2, 5 
# and 8, which results in the sequence of numbers 4, 10 and 16.
#
# value: 0  2  4  6  8  10 12 14 16 18
# index: 0  1  2  3  4  5  6  7  8  9
#              X        X        X
#
print(list(range(0,20,2)[2:10:3]))