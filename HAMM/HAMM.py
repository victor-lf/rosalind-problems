data = open('rosalind_hamm.txt', 'r')
s = data.readline()
t = data.readline()
d_h = 0

for i in range(0, len(s)):
    if s[i] != t[i]:
        d_h += 1

print d_h
data.close()
