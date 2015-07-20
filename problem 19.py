import time
start = time.time()

month = dict()
month[1] = 31
month[3] = 31
month[4] = 30
month[5] = 31
month[6] = 30
month[7] = 31
month[8] = 31
month[9] = 30
month[10] = 31
month[11] = 30
month[12] = 31
x = list()
day = 2

for year in range(1901,2001):
  if year%100 == 0:
    if year%400 == 0: month[2] = 29
    else: month[2] = 28
    for m in range(1,13):
        day = day + month[m] 
        if day%7 == 0:
            if m > 11: x.append((1, 1, year+1))
            else: x.append((m+1, 1, year))
  else:        
    if year%4 == 0: month[2] = 29
    else: month[2] = 28
    for m in range(1,13):
        day = day + month[m] 
        if day%7 == 0:
            if m > 11: x.append((1, 1, year+1))
            else: x.append((m+1, 1, year))
       
print len(x)
elapsed = (time.time() - start)
print elapsed
