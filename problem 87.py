import math
n = 3
i = 0
x = list()
x.append(2)
while n < 7072:
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
    
result = []

for i in range(0,len(x)):
    for j in range(0,len(x)):
        if x[i]**2 + x[j]**3 < 50000000:
            for k in range(0,len(x)):
                if x[i]**2 + x[j]**3 + x[k]**4 < 50000000:
                    s = x[i]**2 + x[j]**3 + x[k]**4
                    result.append(s)
                else:
                    break
        else:
            break

result = {}.fromkeys(result).keys()                
print len(result)
