a = 1
b = 1
while a < 500:
    while b < 500:
        if a*a + b*b == (1000-a-b)*(1000-a-b):
          print a, b
        b = b + 1
    b = 1
    a = a + 1
