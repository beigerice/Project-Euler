def f(x):
    return x * f(x-1) if x >1 else 1
x=list()
y=list()
for i in xrange(0,10):
    x.append(i)
s = f(10)
while s > 0:
    i = 1
    while i <= 10:
        if s-i*f(len(x)-1)<0:
            s = s - (i-1)*f(len(x)-1)
            y.append(x[i-1])
            x.remove(x[i-1])
            break
        if s-i*f(len(x)-1)==0:
            y.append(x[i-1])
            x.remove(x[i-1]) 
            x.reverse()
            y.append((x))
            s = 0
            break
        i = i + 1
print y     
