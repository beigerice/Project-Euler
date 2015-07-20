def is_palindrome(i):
    i = str(i)
    if len(i)%2 == 0:
        for a in range(0,len(i)/2):
            if i[a] != i[len(i)-1-a]:
                return False
                break
            if a == len(i)/2-1:
                return True
    else:
        for a in range(0,len(i)-1/2):
            if i[a] != i[len(i)-1-a]:
                return False
            if a == len(i)/2:
                return True
                break

result = []
for a in xrange(0,1000000):
    b = str(bin(a)).lstrip('0b')
    if is_palindrome(a) and is_palindrome(b):
        result.append(a)
    
print sum(result)
        
