import random

def roll_dice(x, y):
    # Generate two random numbers from 1 to 6 that represents 1 roll of the dice
    return random.randint(x,y)


# Roll 2 dices to represent 
count = 1    
while count <= 6:  
    result1 = roll_dice(1, 6)
    print('Roll: ', count)
    print('1st dice: %s' % (result1))
    dr = (1/6) * 10
    print('Probability', dr)
    result2 = roll_dice(1, 6)
    print('2nd dice:', result2)
    count = count + 1
    
