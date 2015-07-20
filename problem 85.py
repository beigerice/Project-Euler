def reccount(m,n):
    result = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            result += (m-i+1)*(n-j+1)
    return result

result = 100000
area = 1
for i in range(2,100):
    for j in range(2,100):
        temp = 2000000 - reccount(i,j)
        if temp > 0:
            if temp < result:
                result = temp
                area = i*j

print area


