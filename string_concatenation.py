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

string1 = "Good"
string2 = "morning"
string3 = " to you!"

new_string = string1 + " " + string2 + string3

print(new_string)

speed = 20
units = " km/h"

speed_output = str(speed) + units

print(speed_output)

name_list = ["Kamala", "Nageeb", "Sarah"]

names_output = ", ".join(name_list)

print(names_output)

s1 = "good"
s2 = "evening"

good_evening = "{} {}".format(s1, s2)
print(good_evening)

good_evening = "%s %s" % (s1, s2)
print(good_evening)

good_evening = f'{s1} {s2}'
print(good_evening)