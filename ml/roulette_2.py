import matplotlib.pyplot as plt
import random


def random_pop(pop_size, ind_len, genes):
    pop = []
    for _ in range(pop_size):
        pop.append([random.choice(genes) for _ in range(ind_len)])
    return pop


def determine_fitness(pop):
    fitnesses = []
    for ind in pop:
        fitnesses.append(sum(ind))
    total_fitness = sum(fitnesses)
    probs = [fitness / total_fitness for fitness in fitnesses]
    return fitnesses, probs


def plot(pop, probs, title):
    fil_pop = [ind for ind, prob in zip(pop, probs) if prob > 0]
    fil_probs = [prob for prob in probs if prob > 0]

    plt.pie(fil_probs, labels=fil_pop, autopct="%1.1f%%")
    plt.title(title)
    plt.show()


def roulette(pop, probs, num_parents):
    return random.choices(pop, weights=probs, k=num_parents)


genes = [0, 1]
pop_size = 20
ind_len = 5
num_parents = 5

pop = random_pop(pop_size, ind_len, genes)
print(pop)
fitnesses, probs = determine_fitness(pop)
print(fitnesses, probs, sep="\n")
plot(pop, probs, "Initial Population")

parents = roulette(pop, probs, num_parents)
print(parents)
fitnesses, probs = determine_fitness(parents)
print(fitnesses, probs, sep="\n")
plot(parents, probs, "Initial Population")
