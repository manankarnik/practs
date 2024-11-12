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

def tournament(pop, fitnesses, num_parents):
    parents = []
    for _ in range(num_parents):
        i, j = random.sample(range(len(pop)), 2)
        parents.append(pop[i] if fitnesses[i] > fitnesses[j] else pop[j])
    return parents

def mutation():
    return random.choice(genes)

def crossover(parents, pop_size, mutation_rate=0.1):
    offsprings = []
    while True:
        for i in range(0, len(parents), 2):
            p1, p2 = parents[i], parents[i+1]
            c1, c2 = [], []
            for j in range(len(p1)):
                # Crossover: randomly choose gene from either parent
                gene1 = p1[j] if random.random() < 0.5 else p2[j]
                gene2 = p2[j] if gene1 == p1[j] else p1[j]
                
                # Mutation: occasionally alter the gene
                c1.append(mutation() if random.random() < mutation_rate else gene1)
                c2.append(mutation() if random.random() < mutation_rate else gene2)
            offsprings.extend([c1, c2])
            if len(offsprings) >= pop_size:
                return offsprings

genes = list("INDA")
target = list("INDIA")
pop_size = 20
ind_len = 5
num_parents = 4
iterations = 0
use_roulette = True

pop = random_pop(pop_size, ind_len, genes)
print("Initial Population:", pop)

while True:
    fitnesses, probs = determine_fitness(pop, target)
    if use_roulette: parents = roulette(pop, probs, num_parents)
    else: parents = tournament(pop, fitnesses, num_parents)
    print("Fittest parents selected with roulette wheel from the population are: ", parents)
    new_population = crossover(parents, pop_size)
    if use_roulette and sum(fitnesses) > sum(determine_fitness(new_population, target)[0]):
        print("Fitness dropped, switching to tournament selection method")
        use_roulette = False
    population = new_population
    print("The new generation after crossover and mutation is:", population)
    iterations += 1
    if target in population:
        print(f"Target string: INDIA found after {iterations} iterations (Generations).")
        break

