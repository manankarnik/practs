import matplotlib.pyplot as plt
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


def plot(probs, pop, title):
    fil_pop = [ind for prob, ind in zip(probs, pop) if prob > 0]
    fil_probs = [prob for prob in probs if prob > 0]
    
    plt.pie(fil_probs, labels=fil_pop, autopct="%1.1f%%")
    plt.title(title)
    plt.show()


def roulette(pop, probs, num_parents):
    return random.choices(pop, weights=probs, k=num_parents)


genes = list("INDA")
target = list("INDIA")
pop_size = 20
ind_len = 5
num_parents = 4

pop = random_pop(pop_size, ind_len, genes)
print("Initial Population:", pop)
fitnesses, probs = determine_fitness(pop, target)
print("Fitnesses:", fitnesses)
print("Probs:", probs)
plot(probs, pop, "Inital Population")

parents = roulette(pop, probs, num_parents)
print("Parents:", parents)
fitnesses, probs = determine_fitness(parents, target)
print("Fitnesses:", fitnesses)
print("Probs:", probs)
plot(probs, parents, "Parents")


