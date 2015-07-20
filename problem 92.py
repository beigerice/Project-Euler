import itertools
from math import factorial

def square_sum(n):
    s = 0
    for i in str(n):
        s += int(i)*int(i)
    return s

a = [0]*(9*9*7+1)
b = [0]*(9*9*7+1)

a[1] = 1
b[89] = 1

for i in range(2,568):
    j = i
    while True:
        i = square_sum(i)
        if i == 1:
            a[j] += 1
            break
        if i == 89:
            b[j] += 1
            break

print sum(a), sum(b)

result = 0

for comb in itertools.combinations_with_replacement('0123456789',7):
    test = set(comb)
    testc = [comb.count(i) for i in test]
    prod = 1
    for el in testc:
        prod *= factorial(el)
    poss = int(''.join(map(str,comb)))
    if poss == 0: continue
    while True:
        poss = square_sum(poss)
        if a[poss] == 1: break
        if b[poss] == 1:
            result += factorial(7)//prod
            break

print result
