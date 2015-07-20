import math

def gcd(a, b):
  if a < b:
    a, b = b, a

  while b != 0:
    temp = a % b
    a = b
    b = temp

  return a

limit = 1500000
triangles = (limit+1)*[0]

result = 0
mlimit = int(math.sqrt(limit/2))

for m in range(2,mlimit):
    for n in range(1,m):
        if (n+m)%2 == 1 and gcd(n,m) == 1:
            a = m*m + n*n
            b = m*m - n*n
            c = 2*m*n
            p = a + b + c
            while p < limit:
                triangles[p] += 1
                if triangles[p] == 1:
                    result += 1
                if triangles[p] == 2:
                    result -= 1
                p += a+b+c

print result 

