x = list()  

i = 1001
while i < 10000:
    a = i%10
    b =(i%100-i%10)/10
    c =(i%1000-i%100)/100
    d =(i%10000-i%1000)/1000
    if a**5+b**5+c**5+d**5 == i:
        x.append(i)
    i += 1    

i = 10001
while i < 100000:
    a = i%10
    b =(i%100-i%10)/10
    c =(i%1000-i%100)/100
    d =(i%10000-i%1000)/1000
    e =(i%100000-i%10000)/10000
    if a**5+b**5+c**5+d**5+e**5 == i:
        x.append(i)
    i += 1

i = 100001
while i < 200000:
    a = i%10
    b =(i%100-i%10)/10
    c =(i%1000-i%100)/100
    d =(i%10000-i%1000)/1000
    e =(i%100000-i%10000)/10000
    f =(i%1000000-i%100000)/100000
    if a**5+b**5+c**5+d**5+e**5+f**5 == i:
        x.append(i)
    i += 1
    
print sum(x)