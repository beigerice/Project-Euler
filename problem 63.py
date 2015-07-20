import math

def count_digit(n):
    s = 0
    for i in str(n):
        s += 1
    return s

result = 0
for i in range(1,10):
    for j in range(1,50):
        if count_digit(i**j) == j:
            result += 1

print result
        
