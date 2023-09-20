# The Fibonacci sequence is the series of numbers where each 
# number is the sum of the two preceding numbers. 
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, …

def fibonaci(n, a=0, b=1):
    counter = 0
    while counter < n:
        #print('t',b,a)
        a,b = b,a + b
        print(a, end=' ')
        counter = counter + 1
       
fibonaci(10)    