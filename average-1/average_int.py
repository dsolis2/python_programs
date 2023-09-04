# A simple program to find the average of a set of integers

count = int(input("Enter the number of integers to be averaged: "))
i = 0
sum = 0
for i in range(count):
    x = int(input("Enter an integer: "))
    sum = sum + x
avg = sum/count
print("The average is: ", avg)