# Specify the file path to the input dataset
file_path = "/Users/jihane/Downloads/rosalind_tran-5.txt"

# Function to read the FASTA file and extract sequences
def parse_fasta(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split(">")[1:]  # Split by '>'
        sequences = [entry.split("\n", 1)[1].replace("\n", "") for entry in data]
    return sequences

# Function to calculate the transition/transversion ratio
def calculate_ratio(seq1, seq2):
    transitions = 0
    transversions = 0
    # Define purines and pyrimidines
    purines = {"A", "G"}
    pyrimidines = {"C", "T"}
    
    for base1, base2 in zip(seq1, seq2):
        if base1 != base2:  # Mismatch
            if (base1 in purines and base2 in purines) or (base1 in pyrimidines and base2 in pyrimidines):
                transitions += 1  # Transition
            else:
                transversions += 1  # Transversion
    
    return transitions / transversions if transversions > 0 else float("inf")

# Main program
sequences = parse_fasta(file_path)
if len(sequences) == 2:  # Ensure there are exactly two sequences
    seq1, seq2 = sequences
    ratio = calculate_ratio(seq1, seq2)
    print(f"{ratio:.6f}")  # Print with six decimal places
else:
    print("Error: The input file must contain exactly two DNA sequences.")