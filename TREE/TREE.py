with open('rosalind_tree.txt') as data:
    n = int(data.readline())
    adjlist = [[int(a) for a in b.split()] for b in data]
print (n - 1) - len(adjlist)
