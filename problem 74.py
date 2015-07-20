import math

def facsum(n):
    s = 0
    for i in str(n):
        s += math.factorial(int(i))
    return s

#result = []
#for i in range(1000,1000000):
    #k = i
    #chain = []
    #chain.append(i)
    #j = 1
    #while j < 60:
        #i = facsum(i)
        #chain.append(i)
        #chain2 = {}.fromkeys(chain).keys()
        #if len(chain) != len(chain2):
            #chain = chain2
            #break
        #j += 1
    #if len(chain) == 60:
        #print chain
        #result.append(k)

#print len(result)

result = []
for i in range(1000,1000000):
    if facsum(i) == 367945 or facsum(i) == 367954:
        result.append(i)

print len(result)
