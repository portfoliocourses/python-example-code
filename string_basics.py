################################################################################
#
# Program: Introduction To Strings
#
# Description: Examples to introduce the concept of strings and common uses 
# and operations in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=fc3ys0Uo6nY 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Double quote characters can be used to create a string by enclosing characters
# within them... strings are how we represent text data in Python (and many 
# other languages).
programmer = "Grace Hopper"

# Output the string
print(programmer)

# Output the type() of value that the variable programmer references, we'll see
# that the type is <class 'str'>, i.e. a string
print(type(programmer))

# We can also enclose characters within single quote characters to create a 
# string.
computer = 'Harvard Mark 1'

# Output the string
print(computer)

# We can use triple double quote characters to create a multiline string
quote1 = """
A ship in port is safe
but that's not what ships
are built for.
"""

# Output the multiline string
print(quote1)

# We can also use triple single quote characters to create a multiline string
quote2 = '''
It's easier to ask
forgiveness than it is to
get permission.
'''

# Output the multiline string
print(quote2)

# Each character in the string is stored at an index, with the first character
# at index 0, the second character at index 1, and so on.
#
# Index:  0123456789...
school = "Yale University"

# We can use the [] operator to access individual characters in the string by 
# supplying the index... in this case we access the first character 'Y' in the
# above string.
print(school[0])

# Notice that the type returned from school[0] is still string.  Unlike some 
# languages that have a separate type for individual characters, in Python 
# string[index] will simply return a string of one character.
print(type(school[0]))

# We can access the 6th character in the string, 'U'
print(school[5])

# We can use string slicing to specify ranges of indexes in the string and 
# we get back the substring with that range.  If we provide start:end we 
# will get the substring made up of the characters from the start index up 
# until one less than the end index.  So 0:4 will give us back the characters 
# from indexes 0 to 3, i.e. "Yale".
print(school[0:4])

# Providing 5: will give us the substring from index 5 until the end of the 
# string, in this case "University".
print(school[5:])

# The len() function will give us the length of the string, i.e. the number of 
# characters in the string.
print(len(school))

# other_string = "Vassar College"
other_string = "Yale University"

# We can compare strings to check if they are equal using the equality operator,
# try switching which statement above is commented/uncommented to confirm how it
# works.
if (school == other_string):
  print("Schools are the same")
else:
  print("Schools are NOT the same")

# Create a string to test a for loop, as well as 'in' and 'not in below.
text = "invented one of the 1st linkers"

# We can use a for loop with strings to loop over and examine each character in
# the string.  In the below for loop with each loop iteration character will be 
# set to the next character in the string, starting with character 'i' and 
# ending with character 's' in the above string.  In this example we count the 
# occurrences of the character 'e' in the above string.
count = 0
for character in text:
  if (character == "e"):
    count += 1

# Output the count of 'e' characters, which will be 5
print("e count:", count) 

# We can check if a string is a substring of another string using the in 
# operator, in this case "one" is a substring of the string text.
if ("one" in text):
  print("one IS in text")

# We can check if a string is NOT a substring of another string using 'not in',
# in this case "two" is not a substring of the string text.
if ("two" not in text):
  print("two is NOT in text")

# Create a string to test some string methods with below.  Strings have many 
# more methods in Python, but we test some common methods below.
birth = "  Born in New York City  "

# upper() returns the string with all letters converted into uppercase letters
print(birth.upper())

# lower() returns the string with all letters converted into lowercase letters
print(birth.lower())

# strip() when supplied no arguments will return the string with the leading 
# and trailing whitespace characters stripped by default (i.e. removing the 
# spaces at the start and end of the test string).
print(birth.strip())

# replace() allows us to return the string with occurrences of a substring 
# replaced with another string... in this case all occurrences of "York" will
# be replaced with "Fork"
print(birth.replace("York", "Fork"))

# split() will return a list of substrings of the string "split" according to 
# (a) separator character(s), by default the separator is any whitespace 
# characters so below we will get each word in the string above (as thet are 
# each separated by space characters).
print(birth.split())

# Create strings for a first and last name
first_name = "Grace"
last_name = "Hopper"

# We can concatenate strings using the + operator
full_name = first_name + " " + last_name 

# Output the concatenated string, "Grace Hopper"
print(full_name)

# Create a string with placeholders {} where we will dynamically insert values
# as the program is executing using format()
birthday = "{} in the year {}"

# The format method will dynamically insert the values "Born" and 1906 into the
# string where the placeholders are producing the string "Born in the year 1906"
print(birthday.format("Born", 1906)) 

# There are special "escape characters" in Python that may look like multiple 
# characters but are actually one character.  So \n is actually on character, 
# the newline character that represents a new line, it will have the effect of 
# causing Line 2 to be output on the next line (i.e. a new line) in the 
# terminal output.
print("Line 1\nLine 2")