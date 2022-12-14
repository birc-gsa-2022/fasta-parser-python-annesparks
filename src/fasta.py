def fasta_parse(file):
    out = []
    for l in file:
        if l and l[0] == ">":
            trimmed = l[1:].strip()
            out.append([trimmed, ""])
        else:
            out[-1][1] += l.strip()
    return out