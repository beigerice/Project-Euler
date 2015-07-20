def gcd(a, b):
  if a < b:
    a, b = b, a

  while b != 0:
    temp = a % b
    a = b
    b = temp

  return a

result = []
for i in range(9, 1000001):
    j = int(i*3/7)
    while True:
        if gcd(i,j) == 1:
            result.append((float(j)/i,j,i))
            break
        j -= 1

print max(result)
            
    
