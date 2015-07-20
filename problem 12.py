import math
i = 1
while True:
   p = (i*i+i)/2
   x = list()
   j = 1
   while j < math.sqrt(p):
       if p%j == 0:
          x.append(j)
       j = j + 1
   if len(x) > 249:
    print p
    break
   i =  i + 1

   
    
