# These 2 import statements are an example of exporting only functions needed 
# for the program

from random import randint
from collections import Counter

def roll_dice(*dice, trials = 3_000_000):
    pass
    #In Python, underscores are used for user readability only. The Python Interpreter 
    #ignores underscores in numbers. For example, x = 1_000_000 is interpreted to be the same as x = 1000000
    counts = Counter()
    # The underscore in the for loop signals the reader that the value is not important and that the loop is just repeated 10 times
    for _ in range(trials):
        counts[sum((randint(1,sides) for sides in dice))] += 1
      
    for outcome in range(len(dice), sum(dice) +1):
        print((f'{outcome}\t{counts[outcome] *100 / trials :0.2f}%'))    
      
# argument takes in the number of sides, for example, the 4,6,6 = 4 sided die, and two 6 sided dice.
result = roll_dice (4,6,6)
 