# This program uses three different wasy to sort a list of strings


while True:
    words = input('Enter a phrase. To quit the game, type "quit" ')
    if words == 'quit':
        break
    t = words.split()

    print(t)
    t.sort()
    print(t, 'using sort()')
    x = sorted(t)
    print(x, 'using sorted()')
    y = sorted(t, key=lambda v: v.upper())
    print(y, 'using lambda')
    print(' '.join(sorted(words.split(), key=str.casefold)),',using alternate solution')

# alternate solution
#''.join(sorted(words.split(), key=str.casefold))