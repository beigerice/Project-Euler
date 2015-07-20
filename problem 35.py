import math
import time
n = 3
i = 0
x = list()
x.append(2)
while n < 1000000:
  if x[i] <= math.sqrt(n):
     if n%x[i] > 0:
       i = i + 1
     else:
       n = n + 2
       i = 0
  else:
    x.append(n)
    n = n + 2
    i = 0
    
start=time.time()
    
result = list()
y1 = list()
y2 = list()
y3 = list()
y4 = list()
for i in x:    
    if i > 100 and i < 1000:
        if '2' not in str(i) and '5' not in str(i) and '4' not in str(i) and '6' not in str(i) and '8' not in str(i) and '0' not in str(i): 
            y1.append(i)
    if i > 1000 and i < 10000:
        if '2' not in str(i) and '5' not in str(i) and '4' not in str(i) and '6' not in str(i) and '8' not in str(i) and '0' not in str(i): 
            y2.append(i)
    if i > 10000 and i < 100000:
        if '2' not in str(i) and '5' not in str(i) and '4' not in str(i) and '6' not in str(i) and '8' not in str(i) and '0' not in str(i):       
            y3.append(i)
    if i > 100000 and i < 1000000:
        if '2' not in str(i) and '5' not in str(i) and '4' not in str(i) and '6' not in str(i) and '8' not in str(i) and '0' not in str(i):       
            y4.append(i)
        
for i in y1:
    i = str(i)
    if int(i[1]+i[2]+i[0]) in y1:
        if int(i[2]+i[0]+i[1]) in y1:
             result.append(int(i))
             result.append(int(i[1]+i[2]+i[0]))
             result.append(int(i[2]+i[0]+i[1]))
             y1.remove(int(i[1]+i[2]+i[0]))
             y1.remove(int(i[2]+i[0]+i[1]))

for i in y2:
    i = str(i)
    if int(i[1]+i[2]+i[3]+i[0]) in y2:
        if int(i[2]+i[3]+i[0]+i[1]) in y2:
            if int(i[3]+i[0]+i[1]+i[2]) in y2:
                result.append(int(i))
                result.append(int(i[1]+i[2]+i[3]+i[0]))
                result.append(int(i[2]+i[3]+i[0]+i[1]))
                result.append(int(i[3]+i[0]+i[1]+i[2]))
                y2.remove(int(i[1]+i[2]+i[3]+i[0]))
                y2.remove(int(i[2]+i[3]+i[0]+i[1]))
                y2.remove(int(i[3]+i[0]+i[1]+i[2]))

for i in y3:
    i = str(i)
    if int(i[1]+i[2]+i[3]+i[4]+i[0]) in y3:
        if int(i[2]+i[3]+i[4]+i[0]+i[1]) in y3:
            if int(i[3]+i[4]+i[0]+i[1]+i[2]) in y3:
                if int(i[4]+i[0]+i[1]+i[2]+i[3]) in y3:
                    result.append(int(i))
                    result.append(int(i[1]+i[2]+i[3]+i[4]+i[0]))
                    result.append(int(i[2]+i[3]+i[4]+i[0]+i[1]))
                    result.append(int(i[3]+i[4]+i[0]+i[1]+i[2]))
                    result.append(int(i[4]+i[0]+i[1]+i[2]+i[3]))
                    y3.remove(int(i[1]+i[2]+i[3]+i[4]+i[0]))
                    y3.remove(int(i[2]+i[3]+i[4]+i[0]+i[1]))
                    y3.remove(int(i[3]+i[4]+i[0]+i[1]+i[2]))
                    y3.remove(int(i[4]+i[0]+i[1]+i[2]+i[3]))
                    
for i in y4:
    i = str(i)
    if int(i[1]+i[2]+i[3]+i[4]+i[5]+i[0]) in y4:
        if int(i[2]+i[3]+i[4]+i[5]+i[0]+i[1]) in y4:
            if int(i[3]+i[4]+i[5]+i[0]+i[1]+i[2]) in y4:
                if int(i[4]+i[5]+i[0]+i[1]+i[2]+i[3]) in y4:
                    if int(i[5]+i[0]+i[1]+i[2]+i[3]+i[4]) in y4:
                        result.append(int(i))
                        result.append(int(i[1]+i[2]+i[3]+i[4]+i[5]+i[0]))
                        result.append(int(i[2]+i[3]+i[4]+i[5]+i[0]+i[1]))
                        result.append(int(i[3]+i[4]+i[5]+i[0]+i[1]+i[2]))
                        result.append(int(i[4]+i[5]+i[0]+i[1]+i[2]+i[3]))
                        result.append(int(i[5]+i[0]+i[1]+i[2]+i[3]+i[4]))
                        y4.remove(int(i[1]+i[2]+i[3]+i[4]+i[5]+i[0]))
                        y4.remove(int(i[2]+i[3]+i[4]+i[5]+i[0]+i[1]))
                        y4.remove(int(i[3]+i[4]+i[5]+i[0]+i[1]+i[2]))
                        y4.remove(int(i[4]+i[5]+i[0]+i[1]+i[2]+i[3]))
                        y4.remove(int(i[5]+i[0]+i[1]+i[2]+i[3]+i[4]))

print len(result)
print time.time()-start
