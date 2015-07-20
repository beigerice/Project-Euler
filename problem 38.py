result = []
for i in range(123, 1000):
    bad = 0
    if str(i)[0] == str(i)[1] or str(i)[1] == str(i)[2] or str(i)[0] == str(i)[2]:
        continue
    x = []
    x.append(0)
    x.append(int(str(i)[0]))
    x.append(int(str(i)[1]))
    x.append(int(str(i)[2]))
    for j in range(2,4):
        p = i*j
        if p > 1000:
            break
        else:
            for k in range(0,3):
                if int(str(p)[k]) not in x:
                    x.append(int(str(p)[k]))
                else:
                    bad = 1
                    break
            if bad == 1:
                break
        if len(x) == 10:
            result.append(i)

for i in range(5123, 10000):
    bad = 0
    x = []
    x.append(0)    
    for j in range(0,4):
        if int(str(i)[j]) not in x:
            x.append(int(str(i)[j]))
        else:
            bad = 1
            break
    if bad == 1:
        continue
    p = i*2
    for k in range(0,5):
        if int(str(p)[k]) not in x:
            x.append(int(str(p)[k]))
        else:
            break

    if len(x) == 10:
        result.append(i)

print result
