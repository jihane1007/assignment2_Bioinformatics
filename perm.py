from itertools import permutations

# Specify the file path to the input dataset
file_path = "/Users/jihane/Downloads/rosalind_perm.txt"

# Read the input number from the file
with open(file_path, "r") as file:
    n = int(file.read().strip())

# Generate all permutations
nums = list(range(1, n + 1))
all_permutations = list(permutations(nums))

# Print the total number of permutations
print(len(all_permutations))

# Print each permutation
for perm in all_permutations:
    print(" ".join(map(str, perm)))