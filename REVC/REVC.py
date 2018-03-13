string = open('rosalind_revc.txt', 'r')
rev_comp = ""

with open('rosalind_revc.txt') as string:
    for line in string:
        for base in line:
            if base == "A":
                rev_comp = rev_comp + "T"
            if base == "C":
                rev_comp = rev_comp + "G"
            if base == "G":
                rev_comp = rev_comp + "C"
            if base == "T":
                rev_comp = rev_comp + "A"

print rev_comp[::-1]
