a = 2
b = 2
x = list()
while a < 101:
    while b < 101:
        if a**b not in x:
            x.append(a**b)
        b += 1
    b = 2
    a += 1
print len(x)
