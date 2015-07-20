result = []
import math
n = 3
i = 0
x = list()
x.append(2)
while n < 1000:
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
    if i == 2 or i == 5:
        continue
    n = 2
    while True:
        if (10**n-1)%i == 0:
            result.append((n,i))
            break
        n += 1

print sorted(result)
