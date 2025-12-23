
fasta_input = open('/home/florian/Downloads/rosalind_splc.txt').read()

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

def splice_RNA(sequences):
    rna = sequences[0]
    introns = sequences[1:]

    for intron in introns:
        rna = rna.replace(intron, '')

    return rna

def rna_into_protein(rna):
    rna = rna.replace('T', 'U')
    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'AGU': 'S', 'AGC': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '',  'UAG': '',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGA': '',  'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGA': 'R', 'AGG': 'R', 'GGU': 'G', 'GGC': 'G',
        'GGA': 'G', 'GGG': 'G'
    }
    
    protein = ""
    start_found = False
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        amino_acid = codon_table.get(codon, '')
        if codon == 'AUG' and not start_found:
            start_found = True  # Start translation at the first AUG
        if amino_acid == '':
            break  # Stop translation at a stop codon
        if start_found:
            protein += amino_acid
    return protein

spliced_rna = splice_RNA(parse_fasta(fasta_input))
print(spliced_rna)
protein = rna_into_protein(spliced_rna)
print(protein)