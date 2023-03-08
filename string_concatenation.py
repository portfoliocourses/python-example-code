################################################################################
#
# Program: String Concatenation
# 
# Description: Examples of different ways of performing string concatenation 
# in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=28FUVmWU_fA 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################


# test strings
string1 = "Good"
string2 = "morning"
string3 = " to you!"

# The + operator concatenates strings, and we can chain the operator
new_string = string1 + " " + string2

# The += operator will append a string on to the end of a string
new_string += string3

# Together we'll have the new string: "Good morning to you!"
print(new_string)


# test int and string
speed = 20
units = " km/h"

# We can concatenate integers or floating-point values to strings, if we try 
# we'll get a TypeError.  Uncomment the below statement to see!
#
# speed_output = speed + units

# We can convert the value of the other type to a string with str() tohugh, and
# then we can perform the concatenation.
speed_output = str(speed) + units
print(speed_output)


# test list of strings (names)
name_list = ["Kamala", "Nageeb", "Sarah"]

# We can use the join method to join the strings together, separated by a 
# separator string, in this case ", "
names_output = ", ".join(name_list)
print(names_output)


# test strings
s1 = "good"
s2 = "evening"

# The .format() string method can also be used to concatenate strings
good_evening = "{} {}".format(s1, s2)
print(good_evening)

# The % string formatting operator can also be used to concatenate strings
good_evening = "%s %s" % (s1, s2)
print(good_evening)

# And f-strings (i.e. formatted string literals) can also be used to 
# concatenate strings
good_evening = f'{s1} {s2}'
print(good_evening)
