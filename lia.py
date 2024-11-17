def second_law(k, N):
   
    from math import comb

    total_organisms = 2 ** k  
    prob_AaBb = 0.25 

    probability_less_than_N = 0
    for i in range(N):
        probability_less_than_N += comb(total_organisms, i) * (prob_AaBb ** i) * ((1 - prob_AaBb) ** (total_organisms - i))

  
    probability_at_least_N = 1 - probability_less_than_N

    return round(probability_at_least_N, 3)



with open("/Users/jihane/Downloads/rosalind_lia-2.txt", "r") as file:
    data = file.read().strip()
    k, N = map(int, data.split())

# Calculate the result using the given dataset
result = second_law(k, N)
print(result)