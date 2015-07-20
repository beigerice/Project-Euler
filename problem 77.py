import math

n = 3
i = 0
primelist = []
primelist.append(2)
while n < 100:
  if primelist[i] <= math.sqrt(n):
     if n%primelist[i] > 0:
       i += 1
     else:
       n += 2
       i = 0
  else:
    primelist.append(n)
    n += 2
    i = 0

for target in range(10,100):
  x = []
  for prime in primelist:
    if prime < target-1:
      x.append(prime)
  ways = [0]*(target+1)
  ways[0] = 1
  for i in range(0,len(x)):
    for j in range(x[i],target+1):
      ways[j] += ways[j-x[i]]
  if ways[target] > 5000:
    print target
    break
