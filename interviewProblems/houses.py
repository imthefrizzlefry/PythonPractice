''' Demo question from Amazon Demo Assessment

Inspired by the game of life, but in an array rather than a n-dimentional grid.  

each element in the array is a "house" competing with it's neighbors.  Each house has a binary state 1=active 0=inactive.

When both neighbors are either active or inactive, the current house will become inactive.  

The frist and last element in the array have an inactive neighbor outisde of the array.

If a house has one active and one inactive neighbor, then it will be active on the next day.

Given these rules, create a method that will calculate the state after X number of days.

Example:

cellCompete([1],1) -> [0] # this is because the imaginary neighbors to the left and right are both inactive.

cellCompete([1,1], 100) -> [1,1]  # this is because the imaginary neighbors are both inactive, but the real neighbor is active.  So they never change.

cellCompete([1,0,1,1],6) -> [0,0,1,1] -> [0,1,1,1] -> [1,1,0,1] -> [1,1,0,0] -> [1,1,1,0] -> [1,0,1,1] # I iterated through the 6 changes here
'''

def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    if days == 0 or states is None: return states
    
    ret = [0]*len(states)
    for _ in range(days):
        for i in range(len(states)):
            if i == 0:
                ret[i] = 0 if len(states) == 1 or states[i+1] == 0 else 1
            elif i == len(states)-1:
                ret[i] = 0 if states[i-1] == 0 else 1
            else:
                ret[i] = 0 if states[i-1] == states[i+1] else 1
        states = ret[:]
    return ret

print(cellCompete([1,1,1,0,1,1,1,1],2))

print(cellCompete([1],2))

print(cellCompete([1],0))

print(cellCompete([],2))