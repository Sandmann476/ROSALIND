fasta_input = open('data/rosalind_cons (1).txt').read()

def parse_fasta(fasta_str):
    sequences = []
    current_seq = []
    for line in fasta_str.strip().splitlines():
        if line.startswith('>'):
            if current_seq:
                sequences.append(''.join(current_seq))
                current_seq = []
        else:
            current_seq.append(line.strip())
    if current_seq:
        sequences.append(''.join(current_seq))
    return sequences

def consensus_and_profile(sequences):
    n = len(sequences[0])
    profile = {
        'A': [0] * n,
        'C': [0] * n,
        'G': [0] * n,
        'T': [0] * n,
    }

    for seq in sequences:
        for i, nucleotide in enumerate(seq):
            profile[nucleotide][i] += 1

    consensus = ""
    for i in range(n):
        max_count = 0
        max_nuc = ''
        for nuc in "ACGT":
            if profile[nuc][i] > max_count:
                max_count = profile[nuc][i]
                max_nuc = nuc
        consensus += max_nuc

    return consensus, profile

sequences = parse_fasta(fasta_input)
consensus, profile = consensus_and_profile(sequences)

# Output
print(consensus)
for nuc in "ACGT":
    print(f"{nuc}: {' '.join(map(str, profile[nuc]))}")