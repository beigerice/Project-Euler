a = 100
b = 100
x = list()
while a < 1000:
    while b < 1000:
      c = str(a * b)
      if len(c) == 6:
         n1 = float(c[0])
         n2 = float(c[1])
         n3 = float(c[2])
         n4 = float(c[3])
         n5 = float(c[4])
         n6 = float(c[5])
         if n1 == n6 and n2 == n5 and n3 == n4:
           x.append(c)
      b = b + 1
    a = a + 1
    b = a
print max(x)
