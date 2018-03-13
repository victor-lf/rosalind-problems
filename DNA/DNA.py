count_a = 0
count_c = 0
count_g = 0
count_t = 0

with open('rosalind_dna.txt') as string:
    for line in string:
        for base in line:
            if base is ("A"):
                count_a = count_a + 1
            if base is ("C"):
                count_c = count_c + 1
            if base is ("G"):
                count_g = count_g + 1
            if base is ("T"):
                count_t = count_t + 1
    print count_a, " ", count_c, " ", count_g, " ", count_t
