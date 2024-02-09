"""
       Given a list of integers: 1,6,3,10,11
 
       Your stack should look like:
       ---
       11
       ---
       10
       ---
       3
       ---
       6
       ---
       1
       ---

       Implement functions stack.max() which shoudl return max value in the stack. In this
       example stack.max()=11
        
       Also implement stack.pop() which deletes the top value from the stack, in this case 11.
       Now stack.max()=10

       Also implement stack.push(n) to build the stack.
       Also implement stack.peek() to print the stack.

"""


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

# Print max value
val = maxVal(stack)
print("Max value =", val)


#max = maxVal(stack)
#print("Max value =", max)
#print(stack)
#stack.sort(reverse=True) 
#print("Max value =", max)
#print("p =", p)
#stack.append(12)
#print(stack)
#print(max(lst))
#print(lst)
#print(lst.index(1))
#print(lst[0])

for i in range(len(stack)):
   print("---")
   print(stack[i])
    

