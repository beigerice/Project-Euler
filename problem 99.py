import math

input_file = open('base_exp.txt')
result = 0
n = 0
x = 1
y = 1

for line in input_file:
    n += 1
    line = line.rstrip()
    numbers = line.split(',')
    a = float(numbers[0])
    b = float(numbers[1])
    if b * math.log(a) > y * math.log(x):
        x = a
        y = b
        result = n

print x,y,result
