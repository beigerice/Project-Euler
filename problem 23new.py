import time
start=time.time()

limit=20162
sof=[0]*limit
dictionary_abundants = {}
list_abundants = [12]
answer = 0
for i in xrange(1,limit):
    val = i
    while val < limit:
         sof[val] += i
         val += i
for i in xrange(1,limit):
    sof[i] = sof[i] - i

for i in xrange(1,20162):
    if sof[i]>i:
         list_abundants.append(i)
         dictionary_abundants[i] = True
    list_2 = list_abundants
    list_2.reverse()
    for j in list_2:
         if ( (i - j) in dictionary_abundants ):
            break
    else:
         answer += i
print answer    
        
print time.time()-start
