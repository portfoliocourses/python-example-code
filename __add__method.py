################################################################################
#
# Program: __add__ Method Example
# 
# Description: Example of using the __add__ magic method (i.e. dunder method) in
# Python to define how the addition operator (+) should behave for a type of 
# object (i.e. operator overloading).
#
# YouTube Lesson: https://www.youtube.com/watch?v=LlZ-BcrCBZY
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A simple class for representing bank accounts with a balance
class BankAccount:

    # Set the balance attribute to some initial deposit amount
    def __init__(self, initial_deposit):
        self.balance = initial_deposit

    # Output the balance    
    def print_balance(self):
        print("Balance:", self.balance)

    # Defines how the addition operator (+) will behave for BankAccount 
    # objects, where if we have account1 + account2, this method will be 
    # called with "self" set to account1 and "other" set to account2.  We 
    # then have the method return a new BankAccount object with the combined
    # balance of both bank accounts (exactly what we have the __add__method 
    # do is up to us, but this is sensible behaviour).
    def __add__(self, other):
        total = self.balance + other.balance 
        return BankAccount(total)

# Create two bank account objects together
account1 = BankAccount(1000)
account2 = BankAccount(2000)
 
# After adding the two bank accounts we'll find the newly created and returned
# BankAccount object has the combined balance of both BankAccount objects.
new_account = account1 + account2   
new_account.print_balance()