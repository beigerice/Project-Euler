import itertools, math

result = []
prime_list = (2,3,5,7,11,13,17)

for i in itertools.permutations('0123456789',10):
    if i[0] != 0:
        for j in range(1,8):
            if int(i[j]+i[j+1]+i[j+2])%prime_list[j-1] != 0:
                break
            if j == 7:
                n = ''
                for k in range(0,10):
                    n += i[k]
                result.append(int(n))
print result, sum(result)

