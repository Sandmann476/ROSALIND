
data = open("/home/florian/Downloads/rosalind_long(1).txt", "r").read()

def parse_fasta(fasta_str):
    sequences = []
    seq_names = []
    current_seq = []
    for line in fasta_str.strip().splitlines():
        if line.startswith('>'):
            seq_names.append(line[1:].strip())
            if current_seq:
                sequences.append(''.join(current_seq))
                current_seq = []
        else:
            current_seq.append(line.strip())
    if current_seq:
        sequences.append(''.join(current_seq))
    return sequences

def overlap(a, b):
    max_len = min(len(a), len(b))
    for k in range(max_len, 0, -1):
        if a[-k:] == b[:k]:
            return k
    return 0


def shortest_superstring(reads):
    reads = reads[:]

    while len(reads) > 1:
        max_olen = -1
        best_pair = (0, 0)
        merged = ""

        for i in range(len(reads)):
            for j in range(len(reads)):
                if i != j:
                    olen = overlap(reads[i], reads[j])
                    if olen > max_olen:
                        max_olen = olen
                        best_pair = (i, j)
                        merged = reads[i] + reads[j][olen:]

        i, j = best_pair
        new_reads = []
        for k in range(len(reads)):
            if k != i and k != j:
                new_reads.append(reads[k])
        new_reads.append(merged)
        reads = new_reads

    return reads[0]

print(shortest_superstring(parse_fasta(data)))