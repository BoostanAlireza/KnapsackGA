# Genetic algorithm to solve the 0/1 knapsack problem, maximizing value within a weight limit
import random

# List of (value, weight) tuples for items in the knapsack problem
ITEMS = [
    (60, 10),
    (100, 20),
    (120, 30),
    (80, 15),
    (30, 5),
    (50, 10),
    (40, 5),
    (70, 25),
    (90, 35),
    (20, 2)
]

POPULATION_SIZE = 100
GENERATIONS = 100
CROSSOVER_RATE = 0.5
MUTATION_RATE = 0.01
GENOME_LENGTH = len(ITEMS)
MAX_WEIGHT = 50


def create_genome(length):
    # Creates a random binary genome (0 or 1) representing item selection
    return [random.randint(0, 1) for _ in range(length)]

def init_population(population_size, genome_length):
    # Initializes a population of random genomes
    return [create_genome(genome_length) for _ in range(population_size)]

def calculate_fitness(genome):
    # Calculates total value of selected items; returns 0 if weight exceeds MAX_WEIGHT
    total_value = 0
    total_weight = 0

    for gene, (value, weight) in zip(genome, ITEMS):
        if gene == 1:
            total_value += value
            total_weight += weight

    if total_weight > MAX_WEIGHT:
        return 0
    
    return total_value

# Selects a parent using roulette wheel selection based on fitness
def select_parent(population, fitness_values):
    total_fitness_value = sum(fitness_values)

    if total_fitness_value == 0:    # Fallback if all fitnesses are 0
        return random.choice(population)
    
    pick = random.uniform(0, total_fitness_value)
    current = 0

    for individual, fitness_value in zip(population, fitness_values):
        current += fitness_value
        if current >= pick:
            return individual
        

# Performs single-point crossover between two parents with probability CROSSOVER_RATE
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(1, len(parent1) - 1)
        offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
        offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
        return offspring1, offspring2
    return parent1[:], parent2[:]  # Return copies to avoid modifying parents
    

# Mutates each gene with probability MUTATION_RATE by flipping 0 to 1 or 1 to 0
def mutate(genome):
    genome = genome[:]
    for i in range(len(genome)):
        if random.random() < MUTATION_RATE:
            genome[i] = 1 - genome[i]
    return genome

def genetic_algorithm():
    # Counter to stop if best fitness doesn't improve for 5 generations
    counter = 0 

    #An initial population is created
    population = init_population(POPULATION_SIZE, GENOME_LENGTH)

    # Track the best solution found across all generations
    best_fitness_ever = 0
    best_solution_ever = None

    # Evolve over generations
    for generation in range(GENERATIONS):
        fitness_values = [calculate_fitness(genome) for genome in population]

        current_best = max(fitness_values)
        if current_best > best_fitness_ever:
            best_fitness_ever = current_best
            best_index = fitness_values.index(current_best)
            best_solution_ever = population[best_index][:]
            counter = 0 
        else:
            counter += 1
        
        if counter >= 5:
            break
        
        new_population = []
        
        for _ in range(POPULATION_SIZE // 2):
            parent1 = select_parent(population, fitness_values)
            parent2 = select_parent(population, fitness_values)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.extend([mutate(offspring1), mutate(offspring2)])
        
        population = new_population 
        
        print(f'Generation: {generation}: Best Fitness = {current_best}')

    #Shows the items that were chosen to have the best result
    selected_items = [ITEMS[i] for i, gene in enumerate(best_solution_ever) if gene == 1]
    total_weight = sum(weight for _, weight in selected_items)

    print('\nBest Solution:')
    print(f'Total Value: {best_fitness_ever}')
    print(f'Total Weight: {total_weight}')
    print(f'Selected Items: (Value, Weight): {selected_items}')

if __name__ == '__main__':
    genetic_algorithm()