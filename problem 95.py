import math, time

def divsum(n):
    result = 1
    for i in range(2,int(math.sqrt(n))):
        if n%i == 0:
            result += i
            result += n/i
    return result

start = time.time()

limit = 1000000
chain = (limit+1)*[0]
result = [0,0]

for i in range(1,limit):
    temp = []
    temp.append(i)
    while True:
        i = divsum(i)
        if i > limit:
            for j in temp:
                chain[j] = 'i'
            break
        if chain[i] != 0:
            for j in temp:
                chain[j] = 1
            break
        if i in temp:
            for j in temp:
                chain[j] = 1
            if len(temp)-temp.index(i) > result[0]:
                result[0] = len(temp)-temp.index(i)
                result[1] = min(temp[temp.index(i):])
            break
        temp.append(i)
        
    
print result
print time.time()-start



