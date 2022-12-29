################################################################################
#
# Program: String count() Method
# 
# Description: An example of using the string count() method in Python to count
# the occurrences of a string in another string.
#
# YouTube Lesson: https://www.youtube.com/watch?v=0fyn3mocplw 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Create a string for testing purposes
string = "To be or not to be"

# We pass .count() the string that we want to count the occurrences of and 
# .count() will return the occurrences.  We store the occurrences in be_count 
# and output the occurrences using print().  There are 2 occurrences of the 
# word "be" in the string so we get a count of 2.
be_count = string.count("be")
print(be_count)

# Keep in mind that the .count() method doesn't count words in strings, it 
# counts the occurrences of strings in strings.  So below we will only get 
# back that there is one occurrence of the string "to" because the word "To"
# at the start of the string has an uppercase "T", it doesn't match the string
# "to" even though it may be the word "to".
to_count = string.count("to")
print(to_count)

# We can count the occurrences of a character in a string
o_count = string.count("o")
print(o_count) 

# We can supply optional start index and end index arguments to count only the 
# occurrences of a string between the start and end indexes.  Here we count the
# occurrences of the string "o" in between the indexes 2 and 12, and we will get
# back 2 as only two "o" characters occur in this range in the string.
o_range_count = string.count("o",2,12)
print(o_range_count)