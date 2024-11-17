def hamming_distance(s, t):
    # Calculate the Hamming distance between two strings
    return sum(1 for a, b in zip(s, t) if a != b)

# Specify the path to your dataset file
file_path = "/Users/jihane/Downloads/rosalind_hamm.txt"

# Read the file
with open(file_path, "r") as file:
    data = file.read().strip().splitlines()

# First string
s = data[0]
# Second string
t = data[1]

# Compute the Hamming distance
result = hamming_distance(s, t)

# Print the result
print(result)