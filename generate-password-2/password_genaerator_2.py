
import secrets

count = 1
while count <= 5:
    with open("passwords.txt", "r", encoding='utf-8') as f:
        lines = f.readlines()
        random_line = secrets.choice(lines)
        print(''.join(random_line[6:])) 
    count = count +1
