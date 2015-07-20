import math
n = 3
i = 0
x = list()
x.append(2)
while n < 10000:
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
    
odd = 35
while odd < 10000:
    y = list()
    for i in x:
        if len(y) > 0:
            break
        else:
          if i <= odd:
              j = math.sqrt((odd - i)/2)
              if j == int(j):
                y.append(j)
    if len(y) == 0:
        print odd
        break
    odd = odd + 2
