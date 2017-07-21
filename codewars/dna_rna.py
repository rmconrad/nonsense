str = "GATTACA"


def DNAtoRNA(dna):
    return ''.join(map((lambda x: "U" if x == "T" else x), list(dna)))


print DNAtoRNA(str)
