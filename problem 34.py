import math
x=list()

for i in xrange(101,1000):
    if i == math.factorial((i%1000-i%100)/100) + math.factorial((i%100-i%10)/10) + math.factorial(i%10):
        x.append(i)    

for i in xrange(1001,10000):
    if i == math.factorial((i%10000-i%1000)/1000) + math.factorial((i%1000-i%100)/100) + math.factorial((i%100-i%10)/10) + math.factorial(i%10):
        x.append(i)    

for i in xrange(10001,100000):
    if i == math.factorial((i%100000-i%10000)/10000) + math.factorial((i%10000-i%1000)/1000) + math.factorial((i%1000-i%100)/100) + math.factorial((i%100-i%10)/10) + math.factorial(i%10):
        x.append(i)    

for i in xrange(1000001,2540161):
    if i == math.factorial((i%10000000-i%1000000)/1000000) + math.factorial((i%1000000-i%100000)/100000) + math.factorial((i%100000-i%10000)/10000) + math.factorial((i%10000-i%1000)/1000) + math.factorial((i%1000-i%100)/100) + math.factorial((i%100-i%10)/10) + math.factorial(i%10):
        x.append(i) 


print sum(x)
