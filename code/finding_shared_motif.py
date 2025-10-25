data = open("data/rosalind_lcsm (1).txt")

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

#def find_shared_motif(sequences):
#    motif = ""
#    for a in sequences:
#        for n in range(len(a)):
#            for m in range(n + 1, len(a) + 1):
#                candidate = a[n:m]
#                if all(candidate in b for b in sequences):
#                    if len(candidate) > len(motif):
#                        motif = candidate
#    return motif
#This funktion had too high komplexity and took far too long to compute the result

def find_shared_motif(sequences):
    shortest = min(sequences, key=len)
    low, high = 0, len(shortest)
    best_motif = ""

    while low <= high:
        mid = (low + high) // 2
        found = False
        motifs = set(shortest[i:i+mid] for i in range(len(shortest) - mid + 1))

        for motif in motifs:
            if all(motif in seq for seq in sequences):
                found = True
                best_motif = motif
                break

        if found:
            low = mid + 1
        else:
            high = mid - 1

    return best_motif

sequences = parse_fasta(data.read())
shared_motif = find_shared_motif(sequences)
print(shared_motif)