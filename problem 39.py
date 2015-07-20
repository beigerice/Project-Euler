result = []
for p in range(12, 1001):
    x = []
    for a in range(1, p/3):
        for b in range((p-2*a)/2, (p-a)/2):
            if a*a + b*b == (p-a-b)*(p-a-b):
                x.append((a,b,p-a-b))
    result.append((len(x),p))

print sorted(result)
