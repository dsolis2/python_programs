import random

def roll_dice(x, y):
    pass
    # Generate two random numbers from 1 to 6 that represents 2 dice
    return random.randint(x,y)

count = 1    
while count <= 6:
    
    result1 = roll_dice(1, 6)
    print('Roll: ', count)
    print('1st dice: ', result1)
    result2 = roll_dice(1, 6)
    print('2nd dice: ', result2)
    count = count + 1
    
