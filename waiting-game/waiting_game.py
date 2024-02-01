# Waiting game
# 1. Print specified time to beat, ex 4 sec
# 2. input "enter" to start the timer
# 3. Press enter to stop the timer
# 4. Print elapsed time
# 5. if stop time = specified time, print "you win" else print "you lose"
# To format the decimal numbers:
# use %f formater
# example: floatNumber = 1.9876
#          print("%.2f" % floatNumber)
# or use f-string
# example: a = 10.1234
#          f'{a:.2f}'

import time
import random

target = random.randint(2, 4)
print(f'\nYour target time is {target} seconds')


input("---Pres enter to begin---")
start = time.perf_counter()

input(f'\n...Press enter again after {target} seconds')
end = time.perf_counter() - start

if end == target:
    print('You win!')
    print(f'elapsed time {end :.3f}')
else:
    print('You lose!')    
    print('elapsed time ', '%1.2f' % end) # using formatter
    print(f'elapsed time {end :.2f}') # using f-string
    