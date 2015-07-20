import operator  
def c(n,k):  
    return  reduce(operator.mul, range(n - k + 1, n + 1)) /reduce(operator.mul, range(1, k +1))

result = 0

for n in range(10,101):
    for r in range(2,n):
        if c(n,r) > 1000000:
            result += 1

print result
