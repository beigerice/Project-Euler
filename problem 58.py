import math

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

a = 3
b = 2
prime = 0
n = 1

while True:
    diagonal = (a,a+b,a+2*b,a+3*b)
    for i in diagonal:
        if isprime(i):
            prime += 1
    if float(prime)/(4*n+1) < 0.1:
        print 2*n+1
        break
    a += 3*b
    b += 2
    a += b
    n += 1
    
