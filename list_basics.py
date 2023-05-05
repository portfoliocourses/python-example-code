################################################################################
#
# Program: List Basics
# 
# Description: Examples covering the basics of lists in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=k7cVsK5wXTU 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

a = [2,-4,6]

print(a)
print(a[0])
print(a[2])

a[1] = 100 
print(a)

a.append(7)
print(a)

a.insert(1,3)
print(a)

a.extend([8,4])
print(a)

del a[1]
print(a)

a.remove(8)
print(a)

last = a.pop()
print(a)
print(last)

third = a.pop(2)
print(a)
print(third)

print("length:", len(a))

if 8 in a:
    print("8 is in list")
else:
    print("8 is not in list")

a.reverse()
print(a)

a.sort()
print(a)

a.sort(reverse = True)
print(a)

string_list = ["Luke", "Han", "Leia"]
print(string_list)

string_list.sort()
print(string_list)

mixed_list = [2, True, "X", [1,2]]
print(mixed_list)

x = [1,2,3]
y = x 

#        [1,100,3]
#       /      \
#      x        y

y[1] = 100

print("x:", x)
print("y:", y)

q = [1,2,3]
w = q.copy()

#    [1,2,3]      [1,100,3]
#   /            /
#  q            w

w[1] = 100

print("q:", q)
print("w:", w)

#           0    1    2    3    4    5
letters = ["a", "b", "c", "d", "e", "f"]

letters_slice = letters[1:4]

print(letters_slice)

for letter in letters:
    print(letter)

letters.clear()
print(letters)

list1 = [1,2,3]
list2 = [4,5,6]

new_list = list1 + list2 

print(new_list)