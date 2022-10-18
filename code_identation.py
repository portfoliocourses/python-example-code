################################################################################
#
# Program: Code Indentation To Create Code Blocks
#
# Description: Examples of using code indentation to create code blocks in
# Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=CcgSYrWwSpE
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

print("ABC")

# A block of code is a section of Python code that executes as a unit.  Here
# we have an if-statement with a code block that will execute when the
# condition is true (in this case, the condition is always true).  To make the
# code block we indent the statements by 4 space characters.  This is the
# recommended way to indent code in Python according to the official style
# guides.  But we could use other amounts of spaces such as 2 spaces.  And
# we could also use tabs instead of spaces.  We do need to be consistent with
# whatever we use though, we need to use either spaces or tabs (we can't
# mix them), or if we use spaces we need to use the same amonut of spaces.
if (5 > 2):
    print("5 is greater than 2")
    print("2 is less than 5")


# This statement is NOT part of the if-statement code block because it is not
# indented by 4 spaces as those statements are.  If we did indent it by 4
# spaces it would become part of that code block.
print("DONE THE IF!")


if (5 > 2):
    print("5 is greater than 2")
    print("2 is less than 5")

    # We can create a code block within a code block with another layer of
    # indenting, here we indent by another 4 spaces on top of the indent of 4
    # spaces to create this code block within the code block.
    if (2 > 1):
        print("NEW CODE BLOCK")