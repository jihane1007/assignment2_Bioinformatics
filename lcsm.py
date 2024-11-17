def read_fasta(file_path):
    """Reads a FASTA file and returns a list of sequences."""
    sequences = []
    with open(file_path, 'r') as file:
        sequence = ""
        for line in file:
            if line.startswith(">"):
                if sequence:
                    sequences.append(sequence)
                    sequence = ""
            else:
                sequence += line.strip()
        if sequence:
            sequences.append(sequence)
    return sequences

def find_longest_common_substring(sequences):
    """Finds the longest common substring in a list of sequences."""
    # Start with the shortest sequence to minimize comparisons
    shortest_sequence = min(sequences, key=len)
    n = len(shortest_sequence)
    for length in range(n, 0, -1):  # Start with the longest possible substring
        for start in range(n - length + 1):
            substring = shortest_sequence[start:start + length]
            if all(substring in seq for seq in sequences):
                return substring
    return ""

# File path to the dataset
file_path = "/Users/jihane/Downloads/rosalind_lcsm.txt"

# Read the sequences from the FASTA file
sequences = read_fasta(file_path)

# Find and print the longest common substring
longest_common_substring = find_longest_common_substring(sequences)
print(longest_common_substring)