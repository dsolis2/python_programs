
import random

lst = []
for x in range(100):
   lst.append(random.randint(-10, 15))

for num in lst:
    if num < 0:
     print("neg:", num)
    else:
       print("pos: ", num)
        