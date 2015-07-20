import math  
 
def isPrime(n):  
    if n <= 1:
        return False 
    for i in range(2, int(math.sqrt(n)) + 1):  
        if n % i == 0:  
            return False 
    return True

x = list()
a = -999
while a < 1000:
    b = -999
    while b < 1000:
        n = 0
        while True:
            if isPrime(n*n+a*n+b) == False:
                x.append((n,a,b))
                break
            n = n + 1
        b = b + 2
    a = a + 2
print max(x)
