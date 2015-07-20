import time
import math

start = time.time() 
pow = list(str(math.factorial(100)))
n = sum([int(i) for i in pow])
print n

elapsed = (time.time() - start)
print "%s found in %s seconds" % (n,elapsed)
