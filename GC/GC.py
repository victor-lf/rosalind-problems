count_str = 0
count_bp = 0
count_gc = 0
list_ratio = []
list_label = []

with open('rosalind_gc.txt') as fasta:
    for line in fasta:
        if line[0] == ">":
            list_label.append(line[1:])
            count_str += 1
            if count_str > 1:
                ratio = float(count_gc) / count_bp
                list_ratio.append(ratio)
            count_bp = 0
            count_gc = 0
        else:
            count_bp += len(line[:-1])
            for n in xrange(0, len(line[:-1])):
                if line[n] == "C" or line[n] == "G":
                    count_gc += 1

ratio = float(count_gc) / count_bp
list_ratio.append(ratio)

for n in xrange(0, len(list_ratio)):
    if list_ratio[n] == max(list_ratio):
        print list_label[n], max(list_ratio) * 100
