import time
start = time.time()

factors = [0]*1000001
for i in xrange(2,500001):
    val = 2*i
    while val <= 1000000:
        factors[val] += i-1-factors[i]
        val += i

print 1000000*999999/2-sum(factors)

print time.time()-start

