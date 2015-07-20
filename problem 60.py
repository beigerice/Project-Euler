import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if not n % x:
            return False
    return True

n = 3
i = 0
x = []
x.append(2)
while n < 10000000:
  if x[i] <= math.sqrt(n):
     if n%x[i] > 0:
       i = i + 1
     else:
       n = n + 2
       i = 0
  else:
    x.append(n)
    n = n + 2
    i = 0

for i in x:
    if is_prime(int(str(3)+str(i))) == True and is_prime(int(str(i)+str(3))) == True:
        if is_prime(int(str(7)+str(i))) == True and is_prime(int(str(i)+str(7))) == True:
            if is_prime(int(str(109)+str(i))) == True and is_prime(int(str(i)+str(109))) == True:
                if is_prime(int(str(673)+str(i))) == True and is_prime(int(str(i)+str(673))) == True:
                    print i
                    print i+792
                    break
            
