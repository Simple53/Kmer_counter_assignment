def seq(path):

    fasta = {}
    f_raw = open(path, "r+")
    f_out = open(r'C:\EcoliK12_seq.txt', "r+")
    sequence = ''
    head = ''
    for line in f_raw:
        line = line.strip()
        if line.startswith(">"):
            head = line.replace('>', '').split("|")[4]
            fasta[head] = ''
        else:
            sequence += line.strip().replace("\n", "")
            fasta[head] = sequence
            f_out.write(sequence)
    f_raw.close()
    print(fasta.items())
    f_out.close()
    return sequence

if __name__ == '__main__':
    path = r'C:\EcoliK12.fasta'
    seq(path)


