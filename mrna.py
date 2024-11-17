def calculate_mrna_count(protein_string):
    # Codon table with the number of codons for each amino acid
    codon_count = {
        'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2, 'I': 3,
        'K': 2, 'L': 6, 'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6, 'S': 6,
        'T': 4, 'V': 4, 'W': 1, 'Y': 2, 'Stop': 3
    }

    # Initialize total count with Stop codons
    total_count = 3  # Stop codons
    modulo = 1_000_000  # Modulo as per Rosalind's requirement

    # Iterate over the protein string and multiply codon counts
    for aa in protein_string:
        if aa in codon_count:
            total_count = (total_count * codon_count[aa]) % modulo

    return total_count


# Read the protein string from the input file
file_path = "/Users/jihane/Downloads/rosalind_mrna-3.txt"  # Change the path if necessary
with open(file_path, "r") as file:
    protein_sequence = file.read().strip()

# Calculate the result
result = calculate_mrna_count(protein_sequence)

# Print the result
print(result)