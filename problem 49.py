import math
n = 3
i = 0
x = list()
x.append(2)
while n < 10000:
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
y1 = list()
y3 = list()
y7 = list()
y9 = list()
for p in x:
  if p > 1000:
    if p%10 == 1:
      y1.append(p)
    elif p%10 ==3:
      y3.append(p)
    elif p%10 == 7:
      y7.append(p)
    else:
      y9.append(p)
z1 = list()
for p in y1:
  if (p%100-p%10)/10 != (p%1000-p%100)/100 and (p%100-p%10)/10 != (p%10000-p%1000)/1000 and (p%1000-p%100)/100 != (p%10000-p%1000)/1000:
    if (p%100-p%10)/10 != 0 and (p%1000-p%100)/100 != 0:
      z1.append(p)
a = 0
b = 1
final1 = list()
while a < len(z1):
  while b < len(z1):
    if (z1[a]+z1[b])/2 in z1:
      n = list()
      n.append((z1[a]%100-z1[a]%10)/10)
      n.append((z1[a]%1000-z1[a]%100)/100)
      n.append((z1[a]%10000-z1[a]%1000)/1000)
      q = (z1[a]+z1[b])/2
      if (z1[b]%10000-z1[b]%1000)/1000 in n and (z1[b]%1000-z1[b]%100)/100 in n and (z1[b]%100-z1[b]%10)/10 in n:
        if (q%10000-q%1000)/1000 in n and (q%1000-q%100)/100 in n and (q%100-q%10)/10 in n:
          final1.append((z1[a],q,z1[b]))
    b = b + 1
  a = a + 1
  b = a + 1
                   
z3 = list()
for p in y3:
  if (p%100-p%10)/10 != (p%1000-p%100)/100 and (p%100-p%10)/10 != (p%10000-p%1000)/1000 and (p%1000-p%100)/100 != (p%10000-p%1000)/1000:
    if (p%100-p%10)/10 != 0 and (p%1000-p%100)/100 != 0:
      z3.append(p)
a = 0
b = 1
final3 = list()
while a < len(z3):
  while b < len(z3):
    if (z3[a]+z3[b])/2 in z3:
      n = list()
      n.append((z3[a]%100-z3[a]%10)/10)
      n.append((z3[a]%1000-z3[a]%100)/100)
      n.append((z1[a]%10000-z3[a]%1000)/1000)
      q = (z3[a]+z3[b])/2
      if (z3[b]%10000-z3[b]%1000)/1000 in n and (z3[b]%1000-z3[b]%100)/100 in n and (z3[b]%100-z3[b]%10)/10 in n:
        if (q%10000-q%1000)/1000 in n and (q%1000-q%100)/100 in n and (q%100-q%10)/10 in n:
          final3.append((z3[a],q,z3[b]))
    b = b + 1
  a = a + 1
  b = a + 1

z7 = list()
for p in y7:
  if (p%100-p%10)/10 != (p%1000-p%100)/100 and (p%100-p%10)/10 != (p%10000-p%1000)/1000 and (p%1000-p%100)/100 != (p%10000-p%1000)/1000:
    if (p%100-p%10)/10 != 0 and (p%1000-p%100)/100 != 0:
      z7.append(p)
a = 0
b = 1
final7 = list()
while a < len(z7):
  while b < len(z7):
    if (z7[a]+z7[b])/2 in z7:
      n = list()
      n.append((z7[a]%100-z7[a]%10)/10)
      n.append((z7[a]%1000-z7[a]%100)/100)
      n.append((z7[a]%10000-z7[a]%1000)/1000)
      q = (z7[a]+z7[b])/2
      if (z7[b]%10000-z7[b]%1000)/1000 in n and (z7[b]%1000-z7[b]%100)/100 in n and (z7[b]%100-z7[b]%10)/10 in n:
        if (q%10000-q%1000)/1000 in n and (q%1000-q%100)/100 in n and (q%100-q%10)/10 in n:
          final7.append((z7[a],q,z7[b]))
    b = b + 1
  a = a + 1
  b = a + 1

z9 = list()
for p in y9:
  if (p%100-p%10)/10 != (p%1000-p%100)/100 and (p%100-p%10)/10 != (p%10000-p%1000)/1000 and (p%1000-p%100)/100 != (p%10000-p%1000)/1000:
    if (p%100-p%10)/10 != 0 and (p%1000-p%100)/100 != 0:
      z9.append(p)
a = 0
b = 1
final9 = list()
while a < len(z9):
  while b < len(z9):
    if (z9[a]+z9[b])/2 in z9:
      n = list()
      n.append((z9[a]%100-z9[a]%10)/10)
      n.append((z9[a]%1000-z9[a]%100)/100)
      n.append((z9[a]%10000-z9[a]%1000)/1000)
      q = (z9[a]+z9[b])/2
      if (z9[b]%10000-z9[b]%1000)/1000 in n and (z9[b]%1000-z9[b]%100)/100 in n and (z9[b]%100-z9[b]%10)/10 in n:
        if (q%10000-q%1000)/1000 in n and (q%1000-q%100)/100 in n and (q%100-q%10)/10 in n:
          final9.append((z9[a],q,z9[b]))
    b = b + 1
  a = a + 1
  b = a + 1
  
print final9
