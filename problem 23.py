import time
start=time.time()

limit=20162
sof=[0]*limit
x=list()
y=[0]*limit
for i in xrange(1,limit):
    val = i
    while val < limit:
         sof[val] += i
         val += i
for i in xrange(1,limit):
    sof[i] = sof[i] - i
    if sof[i] > i:
        x.append(i)
a = 0
b = 0
while a < len(x):
    while b < len(x):
        if x[a]+x[b]<limit:
            y[x[a]+x[b]] += 1
            b = b + 1
        else:
            break
    a = a + 1
    b = a
z=list()
for i in xrange(1,limit):
    if y[i] == 0:
        z.append(i)
print sum(z)
print time.time()-start
