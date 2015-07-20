import re

count_triangle_word = 0
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

input_file = open('words.txt', 'rU')
for line in input_file:
    word_list = line.split(',')
    for word in word_list:
        letter_list = re.findall(r'\w', word)
        t = word_value(letter_list)
        if int(((1+8*t)**0.5-1)/2) == ((1+8*t)**0.5-1)/2:
            count_triangle_word += 1

print count_triangle_word
