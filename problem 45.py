from math import sqrt
import time
start = time.time()

n = 286
while n < 60000:
    x = n*(n+1)/2
    y = (sqrt(1+24*x)+1)/6
    z = (sqrt(1+8*x)+1)/4
    if y == int(y) and z == int(z):
      print n,x
      break
    n = n + 1

t = time.time()
print t-start
