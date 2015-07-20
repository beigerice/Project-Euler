import math
def digital_sum(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s

result = 0 
for a in range(2, 100):
    for b in range(2, 100):
        n = a**b
        if digital_sum(n) > result:
            result = digital_sum(n)

print result    
