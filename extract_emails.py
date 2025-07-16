################################################################################
#
# Program: Extract Emails From Text
# 
# Description: Extract emails from text using a regular expresion in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=L7OXfdoH80I
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

import re 

# Returns all email addresses found in text.
#
# Uses a pattern to extract all the email addresses from the text using the 
# regular expression module findall function.  Note that the pattern will not 
# match 100% of email addresses due to edge cases, but should match for 99%+ of 
# common email addresses.
#
def extract_emails(text):
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    return re.findall(pattern, text)

# Example text
text = """
    bla bla kevin@gmail.com more text joe.black@canada.ca more 
    text nageeb_ali@company.co.uk
"""

# Test the function
emails = extract_emails(text)
for email in emails:
    print(email)