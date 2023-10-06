# Given a string of characters: 
# 1. when you see ^d you should delete the previous character 
# 2. when you see ^c you should caps the next characters
# 3. when you see ^s you should toggle from caps to lower case or vice versa

# Function to remove the extra ^ and extra letters

def remove(str, y):
    str = list(str)
    str = [x for x in str if x not in (y,'^')]
    str = (''.join(str))
    return str

# when you see ^d you should delete the previous character
str_d = 'Hello World^d'
str_d = remove(str_d, 'd')
print('1.', str_d)

# when you see ^c you should caps the next characters
str_c = 'Hello^cworld'
str_c = remove(str_c, 'c')
str_c = str_c[:5] + ' ' + str_c[5:]
str_c = str_c[:6] + "WORLD"
print('2.', str_c)

# when you see ^s you should toggle from caps to lower case or vice versa
str_s = '^sHello World'
str_s = remove(str_s, 's')
print('3.', str_s.swapcase())