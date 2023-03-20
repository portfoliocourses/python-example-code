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

#       0123456789
text = "Steve Jobs"

new_string = text[12]
print(new_string)

new_string = text[2]
print(new_string)

new_string = text[-1]
print(new_string)

new_string = text[-3]
print(new_string)

new_string = text[1:4]
print(new_string)

new_string = text[1:5]
print(new_string)

new_string = text[0:5]
print(new_string)

new_string = text[:5]
print(new_string)

new_string = text[6:]
print(new_string)

new_string = text[-4:]
print(new_string)

new_string = text[-4:-2]
print(new_string)

new_string = text[0:10:1]
print(new_string)

new_string = text[0:10:2]
print(new_string)

new_string = text[0:10:3]
print(new_string)

new_string = text[::3]
print(new_string)

new_string = text[2::2]
print(new_string)

new_string = text[::-1]
print(new_string)

new_string = text[8:5:-1]
print(new_string)

new_string = text[4::-1]
print(new_string)

new_string = text[:5:-1]
print(new_string)

new_string = text[::-3]
print(new_string)

#             man-5 prod-?     con-3
inventory1 = "12356 423ASDFASF CAN"
inventory2 = "53245 ASFF44 IND"

slice_object = slice(6,-4)

new_string = inventory1[slice_object]  
print(new_string)

new_string = inventory2[slice_object]  
print(new_string)