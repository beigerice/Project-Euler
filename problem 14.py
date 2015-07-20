import time
start = time.time()

limit = 1000000
y = [0] * limit
y[1] = 1
max_length = [1,1]

for i in range(500001,1000000):
  if ((i-1)/3)%2 == 1:
    i = i + 1
    continue
  n,s = i, 0
  x = []
  while n > limit - 1 or y[n] < 1:
     x.append(n)
     if n%2 == 0: n = n/2
     else: n = 3*n + 1
     s += 1
     
  for j in range(s):
    m = x[j]
    if m < limit:
      new = y[n] + s - j
      y[m] = new
      if new > max_length[1]: max_length = [i, new]

print max_length

print (time.time() - start)
