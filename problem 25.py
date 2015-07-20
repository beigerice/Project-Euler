a = 1
b = 1
n = 2
x = list()
while True:
    c = a + b
    n = n + 1
    if a/10**999 >= 1 or b/10**999 >= 1 or c/10**999 >= 1:
        break 
    a = b + c
    n = n + 1
    if a/10**999 >= 1 or b/10**999 >= 1 or c/10**999 >= 1:
        break
    b = c + a
    n = n + 1
    if a/10**999 >= 1 or b/10**999 >= 1 or c/10**999 >= 1:
        break
print n
