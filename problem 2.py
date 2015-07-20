a = 1
b = 2
c = 3
x = list()
while True:
    c = a + b
    if a > 4000000 or b > 4000000 or c > 4000000:
        break
    if c%2 is 0: x.append(c)
    a = b + c
    if a > 4000000 or b > 4000000 or c > 4000000:
        break
    if a%2 is 0: x.append(a)
    b = c + a
    if a > 4000000 or b > 4000000 or c > 4000000:
        break
    if b%2 is 0: x.append(b)  
print x
print sum(x)+2
    
    
