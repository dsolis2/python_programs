# sorting a string
# Take in input of strings (sentence) from the console
# split the strings
# sort the list of strings

while True:
    words = input('Enter a phrase ')
    if words == 'quit':
        break
    t = words.split()
    print(t)
    t.sort()
    print(t, 'using sort()')
    x = sorted(t)
    print(x, 'using sorted()')
    x = sorted(t, key=lambda v: v.upper())
    print(x, 'using lambda')
    print(' '.join(sorted(words.split(), key=str.casefold)),'using alternate solution')

# alternate solution
#''.join(sorted(words.split(), key=str.casefold))