with open('rosalind_rna.txt') as dna:
    for line in dna:
        rna = line.replace('T', 'U')
print rna

# ou, mais simples
#dna = raw_input()
#print (dna.replace('T', 'U'))
