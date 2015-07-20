fraction=[1,1]
for i in range(98,0,-1):
    if i%3 == 2:
        k = 2*int(i/3)+2
        temp = [fraction[0],fraction[1]]
        fraction[0] = temp[1]
        fraction[1] = k*temp[1]+temp[0]
    else:
        k = 1
        temp = [fraction[0],fraction[1]]
        fraction[0] = temp[1]
        fraction[1] = temp[0]+temp[1]
        
temp = [fraction[0],fraction[1]]
fraction[0] = temp[0]+2*temp[1]
fraction[1] = temp[1]

result = 0
for i in str(fraction[0]):
    result += int(i)

print result
