dna_string = ''
match = []
fail_array = []
fail_array.append(0)  # condição P[1]=0

with open('rosalind_kmp.txt') as fasta:
    next(fasta)  # ignora a primeira linha
    for line in fasta:
        dna_string += line.rstrip()

for i in range(1, len(dna_string)):
    for j in range(1, i + 1):
        sub_string = dna_string[j:i + 1]
        if sub_string == dna_string[0:(i - j + 1)]:
            match.append(len(sub_string))
    if match != []:
        fail_array.append(max(match))
    else:
        fail_array.append(0)
    match = []

print fail_array
