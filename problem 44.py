import time
start = time.time()

plist=[n*(3*n-1)/2 for n in xrange(1,2850)]
pset=set(plist)
for j in plist:
  for k in plist[plist.index(j):]:
    s=j+k
    d=k-j
    if s in pset and d in pset: 
      print d 
      break 

t = (time.time() - start)
print t
