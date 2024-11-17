def dominant_phenotype_probability(k, m, n):
    # Total population
    total_combinations = (k + m + n) * (k + m + n - 1)

    # Calculate probabilities for each pair of parents
    prob_dominant = (
        # Two homozygous dominant individuals
        k * (k - 1)
        + # One homozygous dominant and one heterozygous
        2 * k * m
        + # One homozygous dominant and one homozygous recessive
        2 * k * n
        + # Two heterozygous individuals
        0.75 * m * (m - 1)
        + # One heterozygous and one homozygous recessive
        m * n
    ) / total_combinations

    return round(prob_dominant, 5)


# Read the dataset from the file
with open("/Users/jihane/Downloads/rosalind_iprb-2.txt", "r") as file:
    data = file.read().strip()
    k, m, n = map(int, data.split())

# Calculate the result
result = dominant_phenotype_probability(k, m, n)

# Print the result
print(result)

