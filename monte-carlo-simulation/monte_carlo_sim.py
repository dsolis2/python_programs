import random


def roll_dice(x,y,z):
    if x == 4:
         random.randint(1,4)
    if y == 6 or z == 6:
        return random.randint(1,6)   
   

result = roll_dice (4,6,6)
print(result)