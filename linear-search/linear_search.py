'''
Search a list linear checking each element for a match

'''

def search(lst, elmt):
    i = 0
    while i < len(lst):
     if lst[i] == elmt:
        globals()['pos'] = i
        return True
     i = i + 1

    return False    

lst = [5,8,4,6,9,2]
elmt = 9
pos = -1

if search(lst, elmt):
    print('found', elmt, 'at position', pos + 1)
else:
    print('Not found')    