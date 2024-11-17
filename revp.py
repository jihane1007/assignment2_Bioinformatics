# Function to find the reverse complement of a DNA sequence
def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(sequence))

# Function to find reverse palindromes of lengths between 4 and 12
def find_reverse_palindromes(dna_string):
    results = []
    for i in range(len(dna_string)):
        for length in range(4, 13):  # Check lengths from 4 to 12
            if i + length <= len(dna_string):  # Ensure substring is within bounds
                substring = dna_string[i:i+length]
                if substring == reverse_complement(substring):
                    results.append((i + 1, length))  # Store position (1-based) and length
    return results

# Read the DNA sequence from the input file
with open("/Users/jihane/Downloads/rosalind_revp-6.txt", "r") as file:
    lines = file.readlines()
    dna_string = ''.join(line.strip() for line in lines if not line.startswith(">"))  # Skip header if present

# Find and print reverse palindromes
reverse_palindromes = find_reverse_palindromes(dna_string)
for position, length in reverse_palindromes:
    print(position, length)