import random

# Create a random list of integers
lst = []
for x in range(10):
    lst.append(random.randint(0,10))
print(lst)

# find length of list
print("Length of list:", len(lst))

# Find midpoint index of the list
mid = (len(lst)) //2

#find the value of the midpoint
value = lst[mid]
print("value", value)

# sum left side
print("left side ", lst[0:mid])
left = sum(lst[0:mid])
print(left)

# sum right side
print("Right side", lst[mid+1:])
right = sum(lst[mid+1:])
print(right)

# compare left and right
if left < right:
    print("Right side is smaller")
else:
    print("Left side is bigger")    
