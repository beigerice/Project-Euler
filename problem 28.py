x=[]
x.append(1)
d = 1
i = 1
j = 0
while i < 1001:
    n = 1
    j = j + 2
    while n <=4:
        d = d + j
        x.append(d)
        n += 1
    i += 2
print sum(x) 
    
    
    
