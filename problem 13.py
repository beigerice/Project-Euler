input_file = open('13.txt')
s = 0
for line in input_file:
    line = line.rstrip()
    s += int(line)

print s
