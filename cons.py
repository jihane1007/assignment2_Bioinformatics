def read_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        label = None
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                label = line[1:]
                sequences[label] = ""
            else:
                sequences[label] += line
    return sequences

def calculate_profile_matrix(sequences):
    from collections import Counter
    
    sequence_list = list(sequences.values())
    length = len(sequence_list[0])
    profile = {'A': [0] * length, 'C': [0] * length, 'G': [0] * length, 'T': [0] * length}
    
    for i in range(length):
        column = [seq[i] for seq in sequence_list]
        counts = Counter(column)
        for base in "ACGT":
            profile[base][i] = counts.get(base, 0)
    
    return profile

def get_consensus_string(profile):
    consensus = ""
    for i in range(len(profile['A'])):
        max_base = max("ACGT", key=lambda base: profile[base][i])
        consensus += max_base
    return consensus

# Specify the file path
file_path = "/Users/jihane/Downloads/rosalind_cons.txt"

# Process the dataset
sequences = read_fasta(file_path)
profile = calculate_profile_matrix(sequences)
consensus = get_consensus_string(profile)

# Print the results
print(consensus)
for base in "ACGT":
    print(f"{base}: {' '.join(map(str, profile[base]))}")