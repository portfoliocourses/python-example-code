################################################################################
#
# Program: For Loop Examples
# 
# Description: Examples of using for loops in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=AoiUTJrOPRw 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

countries = ["USA", "India", "Canada"]

for country in countries:
    print(country) 

word = "friend"

for letter in word:
    print(letter) 

for i in range(11):
    print(i) 

i = 0
while (i <= 10):
    print(i)  
    i = i + 1

for i in range(5,51,5):
    print(i)

sum = 0
for number in range(1,11):
    print("number:", number)
    sum = sum + number 

print("sum:", sum)

for m in range(1,11):
    for n in range(1,11):
        print(m, "x", n, "=", m * n) 

for i in range(1,11):
    if (i == 5):
        continue
    print(i)
 
for letter in "girl":
    print("letter:", letter)
    if (letter == "t"):
        print("t found")
        break
else:
    print("t not found") 

for i in range(1,11):
    pass