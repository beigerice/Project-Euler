file=open('11.txt')
x = list()
text = file.read()
number = text.split()
for n in number:
    x.append(n)
i = 0
y = list()
for i in range(400):
    if i%20 <= 16:
      p = float(x[i])*float(x[i+1])*float(x[i+2])*float(x[i+3])
      y.append(p)
for i in range(400):
    if i < 340:
      p = float(x[i])*float(x[i+20])*float(x[i+40])*float(x[i+60])
      y.append(p)
      if i%20 <= 16:
          p = float(x[i])*float(x[i+21])*float(x[i+32])*float(x[i+43])
for i in range(400):
    if i < 340 and i%20 >=3:
      p = float(x[i])*float(x[i+19])*float(x[i+38])*float(x[i+57])
      y.append(p)
print max(y)
        
       
       
    
