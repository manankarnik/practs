import random

def random_pop(pop_size, ind_len, genes):
    pop = []
    for _ in range(pop_size):
        pop.append([random.choice(genes) for _ in range(ind_len)])
    return pop


def determine_fitness(pop, target):
    fitnesses = []
    for ind in pop:
        fitness = sum([1 if ind[i] == target[i] else 0 for i in range(len(ind))])
        fitnesses.append(fitness)
    total_fitness = sum(fitnesses)
    probs = [fitness / total_fitness for fitness in fitnesses]
    return fitnesses, probs


def roulette(pop, probs, num_parents):
    return random.choices(pop, weights=probs, k=num_parents)

def mutation():
    return random.choice(genes)

def crossover(parents, mutation_rate=0.1):
    offsprings = []
    for i in range(0, len(parents), 2):
        parent1, parent2 = parents[i], parents[i + 1]
        child1, child2 = [], []
        for j in range(len(parent1)):
            child1.append(parent1[j] if random.uniform(0, 1) < 0.5 else parent2[j])
            child2.append(parent2[j] if child1[-1] == parent1[j] else parent1[j])
            if random.uniform(0, 1) < mutation_rate:
                child1[-1] = mutation()
            if random.uniform(0, 1) < mutation_rate:
                child2[-1] = mutation()
        offsprings.extend([child1, child2])
    return offsprings

genes = list("INDA")
target = list("INDIA")
pop_size = 20
ind_len = 5
num_parents = 4
iterations = 0

pop = random_pop(pop_size, ind_len, genes)
print("Initial Population:", pop)

while True:
    fitnesses, probs = determine_fitness(pop, target)
    parents = roulette(pop, probs, num_parents)
    print("Fittest parents selected with roulette wheel from the population are: ", parents)
    population = crossover(parents)
    print("The new generation after crossover and mutation is:", population)
    iterations += 1
    if target in population:
        print(f"Target string: INDIA found after {iterations} iterations (Generations).")
        break

