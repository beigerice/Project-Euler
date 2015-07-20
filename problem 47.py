import math
import time
n = 3
i = 0
x = list()
x.append(2)
while n < 500000:
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

start = time.time()

c = 210
combo = 0
while c < 500000:
    if combo == 4:
        print c - 1
        break
    d = c
    y = list()
    for i in x:
        if i <= c:
            if c%i == 0:y.append(i)
            while c%i == 0:
                c = c/i
    if len(y) > 3:
        combo = combo + 1
    else:
        combo = 0
    c = d + 1
    
print time.time()-start

      
