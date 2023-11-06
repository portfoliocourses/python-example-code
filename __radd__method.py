################################################################################
#
# Program: __radd__ Method Example
# 
# Description: An example of using the __radd__ magic method (i.e. dunder 
# method) in Python to define how the addition (+) operator should behave for 
# a type of object (i.e. operator overloading) when the object is the right 
# operand of the addition.
#
# YouTube Lesson: https://www.youtube.com/watch?v=UkjKj4AmNhc 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# We'll use Number to check if the other + operand is a type of number in Python
from numbers import Number

# Represents bank accounts
class BankAccount:
    
    # Bank accounts have a balance attribute set to an initial balance
    def __init__(self, initial_balance):
        self.balance = initial_balance 

    # Defines how BankAccount objects should behave with the + operator, both 
    # in the case that both operands are BankAccount objects AND in the case 
    # that the BankAccount is the left operand and a type of number is the 
    # right operand.  The parameter self is the left operand of the 
    # addition operator, and other is the right operand of the addition 
    # operator.  In the case of adding together two BankAccount objects 
    # we return a new BankAccount object with the combined balance, in the
    # case of a BankAccount object added together with a number we return 
    # a new BankAccount object with the sum of the number and the BankAccount
    # operand's balance as the balance of the new BankAccount object. 
    def __add__(self, other):
        # If the right operand is a type of number, we calculate a new total
        # balance by adding the left operand BankAccount balance to the number.
        if (isinstance(other, Number)):
            total = self.balance + other
        # If both operands are BankAccount objects we add both balances to
        # produce the new total
        else: 
            total = self.balance + other.balance 

        # We return a new BankAccount object with the new total.
        return BankAccount(total)

    # The __add__ method will be called if we have:
    #
    # BankAccount + BankAcccount
    #
    # OR
    # 
    # BankAccount + Number   (where Number is some type of number in Python)
    #
    # But if we have...
    #
    # Number + BankAccount
    #
    # then __add__ will NOT be called.  Instead __radd__ will be called 
    # with self set to the right BankAccount operand and other set to 
    # Number.  Because we want + to be commutative (i.e. a + b == b + a) we 
    # can return the result of calling the __add__ method with other/Number
    # as an argument.
    #
    # Note that in general when we have left_operand + right_operand the 
    # __radd__ method of right_operand will be called when either:
    #
    # 1) the __add__ method is not defined for left_operand
    # 2) the __add__ method returns NotImplemented
    #
    def __radd__(self,other):
        return self.__add__(other)

# Create a bank account object
account1 = BankAccount(1000)
 
# Add the bank account to a number, with the bank account as the right operand,
# which will cause __radd__ to be called
new_account = 4000.50 + account1  

# Output the resulting BankAccount object's balance
print(new_account.balance)