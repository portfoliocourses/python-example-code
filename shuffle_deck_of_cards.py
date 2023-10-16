################################################################################
#
# Program: Shuffle A Deck Of Cards
# 
# Description: Example of creating and shuffling a deck of cards using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=9Lh4PAN1HsA 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# We'll represent a deck of cards using a list of tuples, where each tuple 
# contains a suit and rank.
#
# See Deck Of Cards: https://en.wikipedia.org/wiki/Standard_52-card_deck


# Import the random module so we can use the shuffle() function to shuffle the 
# deck of cards.
import random

# A standard deck of card has 4 suits.
suits = ['Heart', 'Diamond', 'Club', 'Spade']

# And each suit has 13 cards of each rank.
ranks = ['Ace', '2', '3', '4', '5', '6', '7',
         '8', '9', '10', 'Jack', 'Queen', 'King']

# Use a list comprehension to produce a list of tuples with 13 cards of each
# rank FOR each suit, for 52 cards total.
deck = [(rank, suit) for suit in suits
                     for rank in ranks]

# The shuffle function from the random module will randomly rearrange the items
# of a list, so by passing deck we will "shuffle the deck".
random.shuffle(deck)

# Output each item in the deck list.  We pass the list using *deck so that each
# item in the list is passed to print() as an individual argument, and then 
# sep="\n" will separate each value output by print by a newline character to 
# output each "card" on a new line.
print(*deck, sep="\n")