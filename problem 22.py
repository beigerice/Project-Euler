import re

result = 0

ldic = {}
ldic['A'] = 1
ldic['B'] = 2
ldic['C'] = 3
ldic['D'] = 4
ldic['E'] = 5
ldic['F'] = 6
ldic['G'] = 7
ldic['H'] = 8
ldic['I'] = 9
ldic['J'] = 10
ldic['K'] = 11
ldic['L'] = 12
ldic['M'] = 13
ldic['N'] = 14
ldic['O'] = 15
ldic['P'] = 16
ldic['Q'] = 17
ldic['R'] = 18
ldic['S'] = 19
ldic['T'] = 20
ldic['U'] = 21
ldic['V'] = 22
ldic['W'] = 23
ldic['X'] = 24
ldic['Y'] = 25
ldic['Z'] = 26

def word_value(n):
    s = 0
    for i in n:
      s += ldic[i]  
    return s

input_file = open('names.txt', 'rU')
for line in input_file:
    name_list = line.split(',')
    name_list = sorted(name_list)
    for i in range(0, len(name_list)):
        letter_list = re.findall(r'\w', name_list[i])
        name_score = word_value(letter_list)*(i+1)
        result += name_score

print result
