################################################################################
#
# Program: Dictionaries Examples
#
# Description: Examples of using the dictionaries built-in data structure in
# Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=cgTUCCEE2Xc 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The deepcopy() function in this module is used to create a deep copy of 
# a dictionary
import copy 

# Dictionaries are made up of key-value pair items
student = {
    "name" : "Grace Hopper",
    "age" : 22,
    "gpa" : 3.7
}

# Output the dictionary
print(student)

# The len() function returns the number of items in the dictionary (3 in this
# case)
print(len(student))

# The type of the dictionary will be 'dict'
print( type(student) ) 

# We can use immutable types as keys as well as tuples made up of numbers, 
# strings and tuples.  We can use any type of object as a key.  So we can 
# use the immutable type boolean values False and True as keys, and 
# mutable list objects as values.
trybools = {False: [1,2,3], True: [4,5,6]}
print(trybools)

# We can use dict() to create dictionary, the keyword argument identifiers
# name and gpa will become string keys in the dictionary.
ada = dict( name = "Ada", gpa = 3.7)
print(ada)

# We can create empty dictionaries with no items...
empty_dictionary = {}
print(empty_dictionary)

# Create another simple dictionary 
course = {
    "name" : "Python 101",
    "average" : 85.5,
}

# We can access values by key using this syntax
print( course["name"] )

# Trying to access a key that does not exist will produce an error
# print( course["teacher"] )

# We can also use .get() to access a value by passing the key as an argument
print( course.get("average") )

# We can update the value for a key like this...
course["average"] = 90.2
print(course["average"])

# We can insert a new key-value pair like this, i.e. a new item...
course["room number"] = 205
print(course)

# We can update the values of a dictionary and insert new items using the 
# update() method...
course.update({"name" : "Python 102",
               "average" : 75.4,
               "teacher" : "Barbara Liskov"})
print(course)

# We can't create a copy of a dictionary by just assigning it to a variable, 
# instead the variable will just reference the same dictionary object in 
# memory.  So if we try to update a value in the dictionary using the variable
# we assigned to, it will actually update the same dictionary that the 
# original variable references... i.e. the dictionary that course references
# will be updated with the key value 'teacher' set to 'Fred'.
variable = course 
variable["teacher"] = "Fred"
print(course)  

# We can use the copy() method to create a (shallow) copy of the dictionary,
# and now course_copy will reference a NEW dictionary object.  So when we 
# update the value at the 'teacher' key, ONLY this copied dictionary object 
# will have its value changed and not the original dictionary object.
course_copy = course.copy()
course_copy["teacher"] = "Joe"
print(course) 
print(course_copy)

# We can loop through the keys of a dictionary with a for loop, and use them
# to access the values in the dictionary (course[key] below).  Each time the 
# loop body executes 'key' will be set to the next key in the dictionary.
for key in course:
    print(key, course[key])

# Create a dictionary and add an additional item to it as well
school = {
    "name" : "Harvard",
    "city" : "Cambridge",
    "country" : "USA"
}
school["founded"] = 1636
print(school)

# The popitem() method will remove the last item added to the dictionary, in 
# this case the item with the key "founded".
school.popitem()
print(school)

# We can use pop() to remove an item with the associated key, in this case the
# item with the key "city".
school.pop("city")
print(school)

# A del statement an also be use to remove an item, in this case the item with 
# the key "country".
del school["country"]
print(school)

# The clear() method will remove all items from the dictionary making it empty.
school.clear()
print(school)

# A del statement can be used to delete the dictionary object itself, so in 
# the below case we can't even use "school" after deleting the dictionary with
# the del statement.
del school
# print(school)

# Create a simple dictionary
x = {"A" : 1, "B" : 2, "C" : 3}

# The keys method will return a view object of the keys in the dictionary
x_keys = x.keys()
print(x_keys)

# The values method will return a view object of the values in the dictionary
x_values = x.values()
print(x_values)

# The items method will return a view object of the key-value pairs in the 
# dictionary as tuples
x_items = x.items()
print(x_items)

# If we modify the items or insert new items into the dictionary, the view 
# objects will ALSO be update.  Here we insert a new item with the key "D" 
# and the value 4.
x["D"] = 4

# If we output the same view objects we'll notice the new item is reflected
# in the output...
print( x_keys )
print( x_values )
print( x_items )

# We can loop through the items in the view objects, for example here we loop
# through the values of the dictionary.
for value in x.values():
    print(value)

# And here we loop through they key-value pairs of the dictionary which are
# tuples of the view object returned by the items() method.
for key, value in x.items():
    print(key, value)

# We can use 'in' to check if a key is in a dictionary
if "E" in x:
    print("E is in x")
else:
    print("E is not in x")

# A dictionary can have a dictionary as a value, we would call this a nested
# dictionary.  Other types of objects can be nested too, e.g. lists.
math_class = {
    "course" : "Calculus",
    "teacher" : {
        "name" : "John Nash"
    }
}

# We use this syntax to access the values of the nested dictionary.
print( math_class["teacher"]["name"] )

# The copy() method creates a shallow copy of the dictionary, what this means
# is that the nested dictionary will not be copied.  Instead, the new copied 
# dictionary created by copy() will reference the SAME nested dictionary as 
# in the original dictionary object.  So if below we change the teacher name
# to "Isaac Newton", this would change the nested dictionary in the original
# dictionary object math_class because it's the same nested dictionary 
# that the math_copy dictionary object references.
#
# math_copy = math_class.copy() 

# If we use the deepcopy() function of the copy module then a deep copy of the
# dictionary will be made, where copies of the nested dictionaries (and other
# objects) will be made too.  So then if later on we modify the teacher name 
# to "Isaac Newton" in the new copied dictionary object, this will not alter
# the teacher name in the original object, because they each have their own
# separate nested dictionaries.
math_copy = copy.deepcopy(math_class)

# Modify the key "name" of the nested dictionary
math_copy["teacher"]["name"] = "Isaac Newton"
 
# Output the original dictionary... because a deep copy was made the nested
# dictionary it contains will not be modified by the above statement.
print(math_class)

# The items in a dictionary are ordered by insertion as of Python 3.7, so these
# two dictionaries have the same items but in different orders.
m = {"x" : 1, "y" : 2}
n = {"y" : 2, "x" : 1} 

# We can see the different orders if we output the dictionaries
print(m)
print(n)

# Notably a check for equality with == will show the dictionaries ARE considered
# equal despite the order of the items being different.
if m == n:
    print("m == n")