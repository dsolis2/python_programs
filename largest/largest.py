'''
Find the largest element in a list

'''
largest = None
#print('Before:', largest)
for iterval in [3, 41, 12, 9, 74, 15, 72, 90]:
    if largest is None or largest < iterval:
        largest = iterval
    #print('Loop:', iterval, largest)
print('Largest:', largest)
