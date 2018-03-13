m = 0
str_list = []
string = ''
sufix_list = []
prefix_list = []
label_list = []

with open('rosalind_grph.txt') as fasta:
    for line in fasta:
        if line.startswith('>'):
            if m > 0:
                str_list.append(string)
                string = ''
            line = line[1:].rstrip('\n')
            label_list.append(line)
        else:
            line = line.rstrip('\n')
            string += line
            m += 1
    str_list.append(string)

for string in str_list:
    sufix_list.append(string[-3:])
    prefix_list.append(string[0:3])

for i in range(len(sufix_list)):
    for n in range(len(prefix_list)):
        if prefix_list[n] == sufix_list[i] and i != n:
            print label_list[i], label_list[n]
