################################################################################
#
# Program: Monty Hall Problem Simulation
#
# Description: A program to simulate the Monty Hall Problem using Python, in 
# particular to test out the different strategies of the player either sticking
# with their original pick OR switching their pick once the host opens a door 
# to reveal the location of a goat.
#
# See the Wikipedia page for more details:
#
#   https://en.wikipedia.org/wiki/Monty_Hall_problem
#
# YouTube Lesson: https://www.youtube.com/watch?v=YNysEWzeseg 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

import random

# The indexes of this list will represent doors with the value at that index 
# representing the result of opening the door
doors = ["goat", "goat", "car"]

# We'll test out the two different strategies of the player either sticking with
# the door they originally picked OR switching doors.  We'll play the game 
# 'attempts' number of times and we should find when the player sticks with 
# their original pick that they win 1/3 of the time but if they switch doors 
# they win 2/3 of the time.
attempts = 100000



# STRATEGY #1 - STICK WITH THE ORIGINAL DOOR

# We'll keep track of how many times the player wins the game, initially 0
wins = 0

# Test what happens when the player stays with their original door pick even
# after the host reveals a goat behind one of the other doors
for i in range(0,attempts):

    # Randomly re-arrange the contents of the doors list to represent the random
    # placement of the goats and car behind the doors
    random.shuffle(doors)

    # The player picks an index (i.e. door) either 0,1,2 in the doors list
    pick = random.randint(0,2) 

    # The host MUST reveal a door with a goat behind it, so we determine which 
    # indexes of the doors list contain a goat and store those into goat_doors
    goat_doors = []
    for j in range(0,3):
        if doors[j] == "goat":
            goat_doors.append(j)
    
    # The first two branches handle the cases where the player picked one of 
    # the doors with a goat behind it... in these cases the host MOST open 
    # the OTHER door with goat behind it, i.e. the only other door with a goat 
    # behind it.  The last branch handles the case where the player picked 
    # the door with the car behind it, in that case the host can open either 
    # door with a goat behind it and so we use choice() to choose one 
    # randomly.
    if pick == goat_doors[0]:
        host_opens = goat_doors[1]
    elif pick == goat_doors[1]:
        host_opens = goat_doors[0]
    else:
        host_opens = random.choice(goat_doors)
    
    # For this strategy the player stays with their original choice and so 
    # the player win if this original 'pick' is where the car is, if so we 
    # increments wins to acknowledge another win has taken place.
    if doors[pick] == "car":
        wins += 1

# Output the win percentage which should be approx. 33% or 1/3 as the player 
# chose 1 of the 3 doors at random and stuck with it and 1 out of the 3 doors 
# has a car behind it.  
print((wins/attempts)*100)



# STRATEGY #2 - SWITCH DOORS AFTER THE HOST REVEALS A GOAT

# Reset wins for testing the other strategy
wins = 0

# Test what happens when the player SWITCHES doors to the only remaining 
# door after the host reveals a door which has a goat behind it...
for i in range(0,attempts):
    
    # Randomly re-arrange the contents of the doors list to represent the random
    # placement of the goats and car behind the doors
    random.shuffle(doors)

    # The player picks an index (i.e. door) either 0,1,2 in the doors list
    pick = random.randint(0,2) 

    # The host MUST reveal a door with a goat behind it, so we determine which 
    # indexes of the doors list contain a goat and store those into goat_doors
    goat_doors = []
    for j in range(0,3):
        if doors[j] == "goat":
            goat_doors.append(j)
    
    # The first two branches handle the cases where the player picked one of 
    # the doors with a goat behind it... in these cases the host MOST open 
    # the OTHER door with goat behind it, i.e. the only other door with a goat 
    # behind it.  The last branch handles the case where the player picked 
    # the door with the car behind it, in that case the host can open either 
    # door with a goat behind it and so we use choice() to choose one 
    # randomly.
    #
    # Now remember that above when the player made their random selection, 
    # there is a 1/3 chance they pick the door with the first goat, a 1/3 
    # chance they pick the door with the other goat, and a 1/3 chance they 
    # pick the door with the car.
    #
    # As we can see below, in the first two branches of the if-elif-else 
    # structure, when the player has picked a door with a goat behind it, 
    # the host is going to open the OTHER door with a goat behind it.  Each
    # of these branches has a 1/3 chance of executing, and so taken together
    # the player has a 2/3 chance that they have initially picked a door with
    # a goat and the host is going to reveal the only other door with a goat
    # behind it.  SO in these two cases, which is 2/3 or 66% of the time, when
    # the player switches their pick to the only other door, that door MUST 
    # contain the car!  
    #
    # When the player does NOT initially pick a door with a goat behind it but
    # instead picks the door with the car, this is covered by the else branch 
    # below, which should only execute/occurs 1/3 of the time.  In this case 
    # the host will reveal one of the two doors with a goat behind it, and the
    # player will switch from the door which has a car to the other door with
    # a goat behind it, and they will lose.  But this will only occur 1/3 of 
    # the time.
    #
    # THIS is why switching leads to a 2/3 probability of winning, and we can
    # see it fairly cleanly when we look at this if-elif-else control structure
    # knowing each branch is equally likely to execute and the first two MUST 
    # lead to the player winning (assuming they switch their pick to the only
    # remaining door).
    # 
    if pick == goat_doors[0]:
        host_opens = goat_doors[1]
    elif pick == goat_doors[1]:
        host_opens = goat_doors[0]
    else:
        host_opens = random.choice(goat_doors)
    
    # Switch to the only remaining door.  We determine the only remaining door
    # by process of elimination.  The three door have indexes 0,1,2, stored in
    # all_doors.  We remove the index the player initially picked as they will 
    # switch away from this pick, and we remove the index for the door the host
    # opened as the player cannot open that door. The only index remaining in 
    # all_doors at index 0 must be the door that the player will switch to.
    all_doors = [0,1,2]
    all_doors.remove(pick)
    all_doors.remove(host_opens)
    switch_pick = all_doors[0]

    # We have the player open the door that they switched to and increment 
    # wins if this is the door with the car
    if doors[switch_pick] == "car":
        wins += 1

# Output the win percentage which should be 2/3 or 66% as discussed above
print((wins/attempts)*100)