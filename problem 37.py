import math, time
start = time.time()

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
result = []
x.append(2)
while n < 1000000:
  if x[i] <= math.sqrt(n):
     if n%x[i] > 0:
       i = i + 1
     else:
       n = n + 2
       i = 0
  else:
    x.append(n)
    if n > 10:
      n = str(n)
      for j in range(1,len(n)):
        if is_prime(int(n[j:])) == False:
          break
        if is_prime(int(n[:j])) == False:
          break
        if j == len(n)-1:
          result.append(int(n))
    n = int(n) + 2
    i = 0

print sum(result)
print time.time()-start
