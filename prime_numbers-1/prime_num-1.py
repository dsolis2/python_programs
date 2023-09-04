# Input - integer value
# output - Return a list containing all of it's prime numbers
# ex: 630 returns a list [2,3,3,5,7]
# product 2*3*3*5*7 = 360


def isDivis(num):
    factors = []
    divisor = 2
    val = num

    while divisor <= num: 
        if num % divisor == 0:
            factors.append(divisor)
            num = num // divisor
        else:
            divisor += 1
    print('prime factors for', val, factors) 
    product = 1
    for x in factors:
        product = product * x 
    print('The product of the factors is', val)      

num = int(input('Enter a number '))
isDivis(num)




    
