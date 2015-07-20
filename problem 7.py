import math
n = 3
i = 0
x = list()
x.append(2)
while len(x) < 10002:
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
print x[10000]

