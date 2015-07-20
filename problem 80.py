from math import sqrt
from decimal import *

getcontext().prec = 100
def digit_sum(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s

for i in range(2,100):
    if sqrt(i) != int(sqrt(i)):
        j = Decimal(sqrt(i))
        print j
        #print digit_sum(j)
