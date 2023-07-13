################################################################################
#
# Program: Find The Frequency Of Each Letter In A String
# 
# Description: Program to find the frequency of each letter in a string and 
# output the results in a nicely formatted table using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=QRIQA0dpVFQ 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

import string

# Prompt the user to enter a string of text, store the returned string into text
text = input("Enter Text: ")

# Will store the total count of all letters in the string
total = 0

# A dictionary to store the count of each letter in the string
counts = {}

# The ascii_lowercase string in the string module that was imported contains the
# lowercase letters a-z in order.  We loop through each letter in this string 
# and set a key in the counts dictionary to zero at this key, each value will 
# be a running count of the number of each letter encountered in the string.
for letter in string.ascii_lowercase:
    counts[letter] = 0

# Loop through each character in the string.  The isalpha() method will return
# true if the current character is a letter.  We count both lowercase and 
# uppercase occurrences of a letter as an occurrence of the same letter, i.e.
# both 'a' and 'A' count as an occurrence of the letter 'a/A'.  So we use the 
# lower() method to turn the letter into a lowercase letter, i.e. if the 
# character is uppercase it will be made lowercase (and if the letter is 
# already lowercase it will remain lowercase).  We then use this lowercase 
# letter to access the key for this letter in the counts dictionary, and we 
# increment the value stored there by 1 to acknowledge we have encountered 
# another occurrence of this letter.  We also increment total by 1 as we have
# encountered another letter.
for character in text: 
    if (character.isalpha()):
        counts[character.lower()] += 1
        total += 1

# Output a newline (and an additional newline as print() does be default) to 
# separate the program input from the output on the terminal by two vertical 
# lines.
print("\n")

# To output a neatly formatted table on the terminal we will output all column 
# headings and associated fields within each row of data with the same field 
# with.  So below we output the column "Letter" with a field width of 9, and 
# then in the for loop below where we output each row of data, we also output 
# the first 'letter' field in each row with a width of 9.  We do this for each
# "column", outputting the Count header and data fields with a width of 9, and 
# the Percentage header and data fields with a width of 12.

# Use an f-string to output the column headings Letter, Count and Percentage 
# with a field width of 9, left aligned via '<', and padded with spaces.
print(f"{'Letter' : <9}{'Count' : <9}{'Percentage' : <12}")

# Output 30 stars for a row to separate the column headings and rows of data. 
# Note how the number of stars matches the combined length of the column 
# widths.
print("******************************") 

# Loop through each letter key in the counts dictionary.  As of Python 3.6 
# onwards dictionaries are ordered by insertion, so because we inserted the 
# keys in the order a-z, we will access the keys in the order a-z using the 
# below loop.  We calculate the percentage of occurrences of the letter 
# relative to the total number of letters.  We then output the letter, the 
# number of occurrences of the letter, and the percentage, in left-aligned 
# fields of width 9,9 and 12, matching the above columns.  Notably in the 
# percentage field we have .2f to output the percentage with fixed point 
# notation and a precision of 2 decimal places.
for letter in counts: 
    percentage = (counts[letter] / total) * 100
    print(f"{letter : <9}{counts[letter] : <9}{percentage : <12.2f}")