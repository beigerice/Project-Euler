target = 200
coinsizes = [1,2,5,10,20,50,100,200]
ways = [0]*(target+1)
ways[0] = 1

for i in range(0,8):
    for j in range(coinsizes[i],target+1):
        ways[j] += ways[j-coinsizes[i]]

print ways[200]
                        
        
