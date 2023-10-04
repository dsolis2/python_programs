'''
Simple program to roll a pair of dice
The program uses a function to randomly to roll 6 sided die.
The function is called twice to simulate 2 dice.

'''

import random

def roll_dice(x, y):
    # Generate two random numbers from 1 to 6 that represents 1 roll of the dice
    return random.randint(x,y)

# Roll 2 dices, 1 call for each roll. The list captures the results for later use
# not yet implemented. This code can be written without a funcion.
lst = list()
count = 1    
while count <= 50:  
    result1 = roll_dice(1, 6)
    lst.append(result1)
    print('Roll: ', count)
    print('1st dice: %s' % (result1))
    result2 = roll_dice(1, 6)
    print('2nd dice:', result2)
    count = count + 1
print('list', lst)    
    
