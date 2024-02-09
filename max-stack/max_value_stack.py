#python

# Initial List
stack = [1,6,3,10,11]

# Reverse the stack to bring highest value to the top of the stack
#stack.sort(reverse=True) 
stack = stack[::-1]
print('Initial stack')
for i in range(len(stack)):
   print("---")
   print(stack[i])

# Max value function
def maxVal(lst):
    return max(lst)

# Print max value
val = maxVal(stack)
print("Max value =", val)

# Remove top value of stack
p = stack.pop(0)
print('Remove top value', p)

# Print max value of new stack
val = maxVal(stack)
print("Max value =", val)

# print final stack
for i in range(len(stack)):
   print("---")
   print(stack[i])
    

