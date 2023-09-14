import random

# Convert list of random numbers to a string
def convert(num):
    s = [str(i) for i in num]
    num = str("".join(s))
    return num

# generate random number
def roll_dice():
    count = 1
    lst = list()
    while count <= 5:
        result = random.randint(1,6)
        lst.append(result)
        count = count + 1
    return lst

def select_word(n):
    i = 1  
    while i <= n:
       lst = roll_dice()
       num = convert(lst) 
       with open("passwords.txt", "r", encoding='utf-8') as f:
        # read all lines in a list
        lines = f.readlines()
        for line in lines:
        # check if string present on a current line
            if line.find(num) != -1:
                print(line[6:])
        i = i + 1
    
select_word(5)    

