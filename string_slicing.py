################################################################################
#
# Program: String Slicing
#
# Description: Examples of using string indexing and slicing in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=nh_BOOfaa44 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Strings in Python are sequences of characters, where each character has an 
# index, with the first character at index 0, for example:
#
#       0123456789
text = "Steve Jobs"

# We can use indexing to create a new string made up of one character of a 
# string.  For example text[0] will give us the string made up of the character
# 'S' from text.
new_string = text[0]
print(new_string)

# Creates string made up of character 'e'
new_string = text[2]
print(new_string)

# Negative indexes will give us a character starting from the end of string, 
# so -1 will give us the last character ('s').
new_string = text[-1]
print(new_string)

# And -3 will give us the 3rd last character 'o'
new_string = text[-3]
print(new_string)

# Indexes will produce an error if they are out of range, so because our string
# only has 10 characters -11 will result in an IndexError.
# new_string = text[-11]
# print(new_string)

# We can use slicing syntax to obtain a new string made up of characters from 
# the original string.  Slicing syntax has start, end and step values separated
# by colons... start:end:step  (though not all values need to be present!)

# Here we use the start index 1 and the end index 4.  This gives us the 
# substring of characters from indexes 1-4 BUT not actually including the 
# character at the end index 4, i.e. "tev"
new_string = text[1:4]
print(new_string)

# With start index 1 and end index 5 we'll get the string "teve"
new_string = text[1:5]
print(new_string)

# With start index 0 and end index 5 we'll get the string "Steve"
new_string = text[0:5]
print(new_string)

# If we leave out the start index the default value used will be 0, so we'll
# again get "Steve"
new_string = text[:5]
print(new_string)

# If we leave out the end index, we'll get the substring up until the end of 
# the string
new_string = text[6:]
print(new_string)

# We can use negative indexes with slicing syntax, so the start index below is
# the index 4 back from the end of the string (i.e. 6) and we'll get "Jobs"
new_string = text[-4:]
print(new_string)

# We can also use negative indexes for the end index, this will result in the
# string "Jo"
new_string = text[-4:-2]
print(new_string)

# This will give us back the entire string as a new string
new_string = text[0:10]
print(new_string)

# The default step value is '1' so if we provide the step value of 1 we'll
# also get back the entire string as a new string
new_string = text[0:10:1]
print(new_string)

# The step (or stride) determines how many characters to jump when reading the
# next character.  So if we provide a step value of 2, we will have every 
# other character in our new string, as we jump 2 characters after reading a 
# character.
new_string = text[0:10:2]
print(new_string)

# A step value of 3 will result in every 3rd character
new_string = text[0:10:3]
print(new_string)

# We can use default start and end indexes when providing a step value as well
new_string = text[::3]
print(new_string)

# Or we can supply just the start index
new_string = text[2::2]
print(new_string)

# If we use a negative step we'll actually jump backwards when reading the next
# character, so the below will actually give us the reversed string!
new_string = text[::-1]
print(new_string)

# When using a negative step, we go backwards in the string, so the start index
# should actually be greater than the end index
new_string = text[8:5:-1]
print(new_string)

# If we don't provide an end index when using a negative step, we'll get the 
# substring up until the beginning of the string.
new_string = text[4::-1]
print(new_string)

# And if we don't provide a start index when using a negative step, we'll get 
# the substring starting from the end of the string.
new_string = text[:5:-1]
print(new_string)

# This will give us every 3rd character from the end of the string to the 
# start of the string.
new_string = text[::-3]
print(new_string)

# We can use the slice() function to return a slice object that we can use in 
# place of using slice syntax.  This allows us to define how to slice a string
# once n a way that's re-usable throughout our program.  The slice() function
# accepts arguments for start, end and step.
#
# Let's imagine we have inventory codes with the format of a 5 digit 
# manufacturing code, followed by a product code of unknown length, and a 
# country code of length 3 characters.  Two examples are given below.  Let's
# also imagine that we wish to extract the product code from the inventory 
# codes.
#
#             man-5 prod-?     con-3
inventory1 = "12356 423ASDFASF CAN"
inventory2 = "53245 ASFF44 IND"

# We can create a slice object using slice.  Here we supply a start index of 6
# and an end index of -4.  This will give us back the product code (whatever 
# length it has).
slice_object = slice(6,-4)

# We can then use the slice object where slice syntax is expected.  The idea 
# is that we can then re-use this throughout program.
new_string = inventory1[slice_object]  
print(new_string)

# Get the product code from the second inventory code.  Notably the slice 
# object will work even if the product codes have different lengths.
new_string = inventory2[slice_object]  
print(new_string)
