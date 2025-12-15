import requests

with open("data/rosalind_mprt (3).txt") as f:
    Prot_ids = [line.strip() for line in f]


def fetch_fasta(uniprot_id):
    if "_" in uniprot_id:
        base_id = uniprot_id.split('_')[0]
    else:
        base_id = uniprot_id
    url = f"https://rest.uniprot.org/uniprot/{base_id}.fasta"
    response = requests.get(url)
    seq = []
    for line in response.text.splitlines():
        if not line.startswith(">"):
            seq.append(line.strip())
    protein = "".join(seq)
    return protein


def find_nglyco_motif(sequence):
    pattern = []
    for i in range(len(sequence) - 3):
            if (
                sequence[i] == "N" and
                sequence[i + 1] != "P" and
                sequence[i + 2] in ("S", "T") and
                sequence[i + 3] != "P"
            ):
                pattern.append(i + 1)  # 1-basiert
    return pattern


def main():
    for Prot_id in Prot_ids:
        sequence = fetch_fasta(Prot_id)
        positions = find_nglyco_motif(sequence)

        if positions:
            print(Prot_id)
            print(" ".join(map(str, positions)))


if __name__ == "__main__":
    main()