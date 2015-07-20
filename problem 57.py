result = 0
fraction = [3,2]
for i in range(1,1001):
    temp = [fraction[0],fraction[1]]
    fraction[0] = temp[0] + 2*temp[1]
    fraction[1] = temp[0] + temp[1]
    numerator = fraction[0]
    denominator = fraction[1]
    if len(str(numerator)) > len(str(denominator)):
        result += 1

print result 
