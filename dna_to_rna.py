
def DNAtoRNA(dna):
    dna_split = dna.split()
    print(dna_split)
    for l in dna_split:
        if l == "T":
            return "U"
        else:
            return l

print DNAtoRNA("GATTACA")




# Works
# def DNAtoRNA(dna):
#     return ''.join(map((lambda x: "U" if x == "T" else x), list(dna)))
