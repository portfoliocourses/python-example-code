################################################################################
#
# Program: __len__ Magic Method
# 
# Description: Example of using the __len__ magic method (i.e. dunder method) 
# in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=bGGXE0D41Nw 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A simple class to represent orders
class Order:
    
    # Orders will have an items attribute set to a list of items in the order
    def __init__(self, items):
        self.__items = items 
    
    # If we supply a definition for the __len__ dunder method, then when objects
    # of this class type are passed to the built-in len() function, this method
    # will be called.  We can define this function however it makes sense for 
    # the type of object we're defining, but the return value does need to be 
    # an integer >= 0.  Here we return the length of the items attribute list.
    def __len__(self):
        return len(self.__items)


# Create an Order object with 3 items.
order = Order(["Pizza", "Pasta", "Salad"])

# We could create an object with 0 items like this.
# order = Order([])

# The built-in len() function will return 3 if we call it with len([1,2,3]),
# but unless if we define a __len__ magic method as above it will not work
# for new object types we define.

# When we call len() and pass it the Order object the __len__ magic method is 
# called and 3 will be returned.  We can output the returned length which we 
# stored into order_length.
order_length = len(order)
print("Length:", order_length)

# Objects will evaluate to a boolean value True or False when used in situations
# like if-statement conditions.  If no __bool__ AND no __len__ magic methods are
# defined, the object will default to the value of True.  If a __bool__ magic 
# method is defined, this method will be called to return either True or False.
# If no __bool__ magic method is defined BUT a __len__ magic method IS defined
# then this method will be called, and if returns 0, the object will evaluate
# to False, otherwise if it returns a number greater than 0, the object will
# evaluate to False.
#
# So if we have an Order object with 3 items we'll get True below.  If we 
# instead had an Order object with 0 items we would get False below.
#
if order:
    print("order is True")
else:
    print("order is False")