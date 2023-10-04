'''
Use binary algorithm to search through a string
This example dynamically creates a list in ascending
order as the input list and a randomly created key to 
search

'''

import random

# declare starting postion at -1
pos = -1

def search(lst, n):
    l = 0
    u = len(lst) - 1

    while l <= u:
        # find the mid value
        mid = (l + u) // 2
        if lst[mid] == n:
            # use globals() to call variable from outside the function
            globals() ['pos'] = mid
            return True
        else: 
            # compare the lower values
            if lst[mid] < n:
                l = mid + 1
            # compare the upper values     
            else:
                u = mid - 1
    return False             

# Test list
lst = [x for x in range(1000000)]

# Random Key value to search
key = random.randint(0, 1000000)

if search(lst, key):
    print('Found', key, 'at position', pos + 1)
else:
    print('Not found')
