from math import sqrt

result = 9
for d in range(2,1001):
    if sqrt(d) ==  int(sqrt(d)):
        continue
    y = 1
    while True:
        if sqrt(1+d*y**2) == int(sqrt(1+d*y**2)):
            x = sqrt(1+d*y**2)
            print x, y, d
            if x > result:
                result = x
            break
        y += 1

print result
