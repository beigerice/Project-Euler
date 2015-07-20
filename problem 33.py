result = []
for a in range(11, 99):
    for b in range(a+1, 100):
        if a%10 == 0 or b%10 == 0: continue
        if a%10 == (b-b%10)/10:
            if float(a-a%10)/10/(b%10) == float(a)/b:
                result.append((a,b))
print result
