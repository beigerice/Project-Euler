import math
i = 3
x = list()
y = 600851475143
while i < math.sqrt(600851475143):
    while y % i == 0:
        x.append(i)
        y = y/i
    i = i + 2
print x
print max(x)
        
        
