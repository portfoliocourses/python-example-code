################################################################################
#
# Program: Partition A String Using partition() and rpartition() String Methods
# 
# Description: Examples of using the partition() and rpartition() string methods
# in Python to partition a string according to a separator string.
#
# YouTube Lesson: https://www.youtube.com/watch?v=ZAr7ebZJ75w 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The partition() method accepts a separator string as an argument, and it will 
# return a tuple containing the string leading up to the first occurrence of 
# the separator string, followed by the separator string, followed by the 
# remainder of the string.  So for the below call the method will return the 
# tuple:
#
# ('A miss is ', 'as', ' good as a mile')
# 
string = "A miss is as good as a mile"
tuple = string.partition("as")
print(tuple)

# If the separator string cannot be found in the original string we will get 
# back a tuple containing the original string as the first item followed by 
# two empty string as the next two items.  So for the below call the method 
# will return the tuple:
#
# ('A miss is as good as a mile', '', '')
#
string = "A miss is as good as a mile"
tuple = string.partition("notthere")
print(tuple)

# The rpartition() method will partition the string based on the LAST occurrence
# of the separator string instead of the first.  Again it accepts the separator
# string as an argument and returns the tuple containing the string leading up 
# to the last occurrence of the separator string, followed by the separator 
# string, followed by the remainder of the string.  So for the below the 
# method will return the tuple:
#
# ('A miss is as good ', 'as', ' a mile')
# 
string = "A miss is as good as a mile"
tuple = string.rpartition("as")
print(tuple)

# If the separator string cannot be found in the original string we will get 
# back a tuple containing the empty string as the first two items followed by
# the original string as the last item of the tuple.  So for the below call the 
# method will return the tuple:
#
# ('', '', 'A miss is as good as a mile')
#
string = "A miss is as good as a mile"
tuple = string.rpartition("notthere")
print(tuple)