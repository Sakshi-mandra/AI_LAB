'''
lab8 : Implement the Genetic Algorithm
'''
import random

# Parameters
POP_SIZE = 6
GENE_LENGTH = 5   # 5 bits: represents numbers 0 to 31
GENERATIONS = 10
MUTATION_RATE = 0.05

# 1. Initialize Random Population (e.g., ['01101', '10001', ...])
population = [''.join(random.choice('01') for _ in range(GENE_LENGTH)) for _ in range(POP_SIZE)]

for gen in range(1, GENERATIONS + 1):
    # 2. Decode Binary to Integer and Calculate Fitness (f(x) = x^2)
    decoded = [int(chrom, 2) for chrom in population]
    fitness = [x**2 for x in decoded]
    
    # Track the best solution in this generation
    best_fit = max(fitness)
    best_chrom = population[fitness.index(best_fit)]
    print(f"Generation {gen:2d} | Best: {best_chrom} (x = {int(best_chrom, 2):2d}) | Fitness = {best_fit}")

    # 3. Selection (Roulette Wheel)
    total_fit = sum(fitness) or 1
    probs = [f / total_fit for f in fitness]
    
    # Pick parents based on fitness probability
    selected_parents = random.choices(population, weights=probs, k=POP_SIZE)

    # 4. Crossover & Mutation (Create Next Generation)
    next_gen = []
    for i in range(0, POP_SIZE, 2):
        p1, p2 = selected_parents[i], selected_parents[i+1]
        
        # Single-point crossover
        cut = random.randint(1, GENE_LENGTH - 1)
        c1 = p1[:cut] + p2[cut:]
        c2 = p2[:cut] + p1[cut:]

        # Bit-flip mutation
        def mutate(chrom):
            return ''.join(
                ('1' if bit == '0' else '0') if random.random() < MUTATION_RATE else bit
                for bit in chrom
            )

        next_gen.extend([mutate(c1), mutate(c2)])
    
    population = next_gen