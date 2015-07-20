import math
an = list()
for i in range(4,10001):
    if i in an:
        continue
    x = list()
    x.append(1)
    for a in range(2,int(math.sqrt(i))+1):
        if i%a == 0:
            if i/a > a:
                x.append(a)
                x.append(i/a)
            elif i/a == a:
                x.append(a)
    j = sum(x)
    if j != i:
        y = list()
        y.append(1)
        for b in range(2,int(math.sqrt(j))+1):
            if j%b == 0:
                if j/b > b:
                    y.append(b)
                    y.append(j/b)
                elif j/b == b:
                    y.append(b)
    if sum(y) == i:
        an.append(i)
        an.append(j)
print an, sum(an)
    
