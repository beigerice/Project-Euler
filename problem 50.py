import time
import math


n = 3
i = 0
x = list()
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
    n = n + 2
    i = 0
    
start = time.time()    
m = 543
s = 0
while s < len(x)-m+1:
  a = 0
  for j in range(s,m+s):
    a = a + x[j]
  if a > 999999:
    break
  if a in x:
    print a,m,x[s],x[m+s-1]
    break
  s = s + 1
  
elapsed = (time.time() - start)
print elapsed
