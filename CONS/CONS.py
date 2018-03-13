cons = []
str_list = []
string = ''

with open('rosalind_cons.txt') as fasta:
    for line in fasta:
        if line[0] != '>':
            line = line.rstrip('\n')
            string += line
        elif string != '' and line[0] == '>':
            str_list.append(string)
            string = ''
    str_list.append(string)

count_a = [0] * len(string)
count_c = [0] * len(string)
count_g = [0] * len(string)
count_t = [0] * len(string)

for string in str_list:
    for i in range(0, len(string)):
        if string[i] == 'A':
            count_a[i] += 1
        if string[i] == 'T':
            count_t[i] += 1
        if string[i] == 'C':
            count_c[i] += 1
        if string[i] == 'G':
            count_g[i] += 1

for i in range(0, len(string)):
    l = [count_a[i], count_c[i], count_g[i], count_t[i]]
    if max(l) == count_a[i]:
        cons.append('A')
    if max(l) == count_c[i] and count_c[i] != count_a[i]:
        cons.append('C')
    if max(l) == count_g[i] and count_g[i] != count_a[i] and\
       count_g[i] != count_c[i]:
        cons.append('G')
    if max(l) == count_t[i] and count_t[i] != count_a[i] and\
       count_t[i] != count_c[i] and count_t[i] != count_g[i]:
        cons.append('T')

print ''.join(cons)
print 'A:', ' '.join(map(str, count_a))
print 'C:', ' '.join(map(str, count_c))
print 'G:', ' '.join(map(str, count_g))
print 'T:', ' '.join(map(str, count_t))
