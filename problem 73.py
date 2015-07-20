def gcd(a, b):
  if a < b:
    a, b = b, a

  while b != 0:
    temp = a % b
    a = b
    b = temp

  return a

result = 0
for i in range(5,12001):
    lowerlimit = int(i/3)+1
    upperlimit = int(i/2)
    for j in range(lowerlimit,upperlimit+1):
        if gcd(i,j) == 1:
            result += 1

print result 
    
