def reverse_complement(dna):
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(comp[b] for b in reversed(dna))


codon_table = {
    'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
    'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
    'ATT':'I','ATC':'I','ATA':'I','ATG':'M',
    'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
    'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
    'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
    'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
    'TAT':'Y','TAC':'Y','TAA':'Stop','TAG':'Stop',
    'CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAT':'N','AAC':'N','AAA':'K','AAG':'K',
    'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
    'TGT':'C','TGC':'C','TGA':'Stop','TGG':'W',
    'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGT':'S','AGC':'S','AGA':'R','AGG':'R',
    'GGT':'G','GGC':'G','GGA':'G','GGG':'G'
}


def find_orfs(dna):
    proteins = set()
    for frame in range(3):
        i = frame
        while i <= len(dna) - 3:
            codon = dna[i:i+3]
            if codon == 'ATG':
                protein = []
                j = i
                while j <= len(dna) - 3:
                    curr = dna[j:j+3]
                    aa = codon_table[curr]
                    if aa == 'Stop':
                        proteins.add(''.join(protein))
                        break
                    protein.append(aa)
                    j += 3
            i += 3
    return proteins


def open_reading_frames():
    lines = open("/home/florian/Downloads/rosalind_orf(2).txt").read().strip().splitlines()
    dna = ''.join(line.strip() for line in lines if not line.startswith('>'))
    rc = reverse_complement(dna)
    return find_orfs(dna) | find_orfs(rc)

results = open_reading_frames()

for protein in results:
    print(protein)
