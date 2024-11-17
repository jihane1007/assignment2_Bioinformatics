def read_fasta(file_path):
    fasta_dict = {}
    with open(file_path, "r") as file:
        label = ""
        sequence = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if label:
                    fasta_dict[label] = sequence
                label = line[1:]  # Remove '>'
                sequence = ""
            else:
                sequence += line
        if label:
            fasta_dict[label] = sequence
    return fasta_dict

def transcribe_and_translate(file_path):
    fasta_sequences = read_fasta(file_path)
    dna_sequence = ""
    introns = []
    for label, sequence in fasta_sequences.items():
        if not dna_sequence:
            dna_sequence = sequence
        else:
            introns.append(sequence)

    # Remove introns from the DNA sequence
    for intron in introns:
        dna_sequence = dna_sequence.replace(intron, "")

    # Define RNA codon table
    codon_table = {
        "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
        "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
        "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
        "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
        "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
        "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
        "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
        "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
        "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
        "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
        "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
        "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
        "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
        "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
        "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
        "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
    }

    # Convert DNA to RNA
    rna_sequence = dna_sequence.replace("T", "U")

    # Translate RNA to protein
    protein = ""
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i + 3]
        amino_acid = codon_table.get(codon, "")
        if amino_acid == "Stop":
            break
        protein += amino_acid

    return protein

# Specify the full path to the dataset file
file_path = "/Users/jihane/Downloads/rosalind_splc-3.txt"  # Change this to the correct file path

# Call the function and print the result
protein_string = transcribe_and_translate(file_path)
print(protein_string)