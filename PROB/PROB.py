import math

gc_label = []
log = []

with open('rosalind_prob.txt') as data:
    dna_string = data.readline().rstrip()
    gc_contents = [float(n) for n in data.readline().rstrip().split()]

prob = [1] * len(gc_contents)

for i in range(len(dna_string)):
    if dna_string[i] == 'G' or dna_string[i] == 'C':
        gc_label.append(1)
    else:
        gc_label.append(0)

for i in range(len(gc_contents)):
    for j in range(len(dna_string)):
        if gc_label[j] == 1:
            prob[i] *= float(gc_contents[i]) / 2
        else:
            prob[i] *= float(1 - gc_contents[i]) / 2
    log.append(math.log10(prob[i]))

print ' '.join(map(str, log))
