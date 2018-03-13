n, k = 35, 4
seq = [1, 1]

for i in range(2, n):
    seq.append(seq[i - 1] + (k * seq[i - 2]))

print seq[-1]
