# Define the monoisotopic mass table for amino acids
mass_table = {
    'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
    'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406,
    'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
    'P': 97.05276,  'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
    'T': 101.04768, 'V': 99.06841,  'W': 186.07931, 'Y': 163.06333
}

# Function to calculate the total weight of a protein string
def calculate_protein_mass(protein):
    total_mass = 0
    for amino_acid in protein:
        total_mass += mass_table[amino_acid]
    return round(total_mass, 3)

# Read the protein string from the file
with open("/Users/jihane/Downloads/rosalind_prtm-3.txt", "r") as file:
    protein_string = file.read().strip()

# Calculate the mass and print it
result = calculate_protein_mass(protein_string)
print(result)