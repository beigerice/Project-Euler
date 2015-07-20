import math
def readd(n):
    re = 0
    for i in range(0,len(str(n))):
        re += int(10**i*int(str(n)[i]))
    result = n + re
    return result

def ispali(n):
    re = 0
    for i in range(0,len(str(n))):
        re += int(10**i*int(str(n)[i]))
    if n == re:
        return True
    else:
        return False

result = []
for i in range(10,10000):
    n = i
    j = 0
    while True:        
        n = readd(n)
        if ispali(n):
            break
        j += 1
        if j == 50:
            result.append(i)
            break

print len(result), result
