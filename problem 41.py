import itertools, math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if not n % x:
            return False
    return True

p = 0
result = []

for i in itertools.permutations('234567',6):
    p = int(i[0])*10**6+int(i[1])*10**5+int(i[2])*10**4+int(i[3])*10**3+int(i[4])*100+int(i[5])*10+1
    if is_prime(p):
        result.append(p)

for i in itertools.permutations('124567',6):
    p = int(i[0])*10**6+int(i[1])*10**5+int(i[2])*10**4+int(i[3])*10**3+int(i[4])*100+int(i[5])*10+3
    if is_prime(p):
        result.append(p)

for i in itertools.permutations('123456',6):
    p = int(i[0])*10**6+int(i[1])*10**5+int(i[2])*10**4+int(i[3])*10**3+int(i[4])*100+int(i[5])*10+7
    if is_prime(p):
        result.append(p)
        

print max(result)
