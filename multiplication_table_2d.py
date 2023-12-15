################################################################################
#
# Program: Print A 2D Multiplication Table
#
# Description: A program to print a 2D multiplication table using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=G_3KSbpXjZM 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# This program outputs multiplication tables like the 10x10 table below where 
# the numbers of the first row are multiplied by the numbers of the first 
# column to give us the product of each, i.e. 6 x 4 = 24. 
#
#    x    1    2    3    4    5    6    7    8    9   10
#    1    1    2    3    4    5    6    7    8    9   10
#    2    2    4    6    8   10   12   14   16   18   20
#    3    3    6    9   12   15   18   21   24   27   30
#    4    4    8   12   16   20   24   28   32   36   40
#    5    5   10   15   20   25   30   35   40   45   50
#    6    6   12   18   24   30   36   42   48   54   60
#    7    7   14   21   28   35   42   49   56   63   70
#    8    8   16   24   32   40   48   56   64   72   80
#    9    9   18   27   36   45   54   63   72   81   90
#   10   10   20   30   40   50   60   70   80   90  100

# Prompt the user to enter the table dimension, convert the string returned by 
# input() into an into and store it into dimension
dimension = int(input("Enter Table Dimension (1...99): "))
 
# If the dimension is in the acceptable range, output the table
if dimension >= 1 and dimension <= 99:

    # All products, row/column headers and 'x' are output into fields of width 
    # 5 characters so that table columns will have a consistent width.  Notably
    # 99 x 99 = 9801 and so the max possible dimension of 99 is compatible with 
    # this field width.

    # Output the 'x' in the first row into a field of width 5 characters, 
    # right-aligned, using an f-string.  > makes it right-aligned.  We also 
    # use the keyword argument end to alter the default behavior of print(),
    # this will stop it from outputting a newline \n so we can continue to 
    # output the column headings on this row.
    print(f"{'x':>5}", end="") 

    # Output the column headings from 1...dimension, again into fields of width
    # 5 characters, right-aligned by default as they are integers.
    for n in range(1, dimension + 1):
        print(f"{n:5}", end="")

    # Output a newline so next table row begins on the next row of the terminal
    # (remember print() outputs a newline by default after the string it is 
    # passed as an argument)
    print("")

    # Loop to create rows from 1...dimension
    for n in range(1, dimension + 1):

        # Output the row heading 'n' (1,2,3,... which each loop iteration)
        print(f"{n:5}", end="")

        # On this same row, output the products of multiplying this row's 
        # number 'n' with the column numbers i=1,2,...,n
        for i in range(1, dimension + 1):
            print(f"{i*n:5}", end="")

        # Output a newline at the end of each table row so the next row outputs
        # on the next line of the terminal 
        print("")

# Otherwise output an error message if dimension not in range
else:
    print("Dimension must be in the range 1...99")