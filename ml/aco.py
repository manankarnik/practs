import random

# Parameters
vertices = ['A', 'B', 'C', 'D']
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'B', 'C']
}
weights = {
    'AB': 10, 'AC': 10, 'AD': 30,
    'BC': 40, 'BD': 10, 'CD': 20
}
num_ants = 4
num_iterations = 10
decay_rate = 0.1
alpha = 1    # Influence of pheromone
beta = 2     # Influence of heuristic (inverse of weight)

# Initialize pheromones
pheromones = {edge: 1 for edge in weights.keys()}

# Function to calculate the probability for choosing next node
def calculate_probability(current, next_vertex):
    key = ''.join(sorted([current, next_vertex]))
    pheromone = pheromones[key] ** alpha
    heuristic = (1 / weights[key]) ** beta
    return pheromone * heuristic

# Main ACO loop
for iteration in range(num_iterations):
    all_paths = []
    for ant in range(num_ants):
        current_vertex = random.choice(vertices)
        path = [current_vertex]
        visited = set(path)

        # Construct a path for the ant
        while len(visited) < len(vertices):
            choices = [(v, calculate_probability(current_vertex, v)) for v in graph[current_vertex] if v not in visited]
            total_prob = sum(prob for _, prob in choices)
            if total_prob == 0:
                break
            # Choose next vertex based on probability
            next_vertex = random.choices([v for v, _ in choices], [prob / total_prob for _, prob in choices])[0]
            path.append(next_vertex)
            visited.add(next_vertex)
            current_vertex = next_vertex
        all_paths.append(path)

    # Print each ant's path
    print(f"Iteration {iteration + 1}: Paths of each ant: {all_paths}")

    # Decay pheromones
    for edge in pheromones:
        pheromones[edge] *= (1 - decay_rate)

    # Update pheromones based on path lengths
    for path in all_paths:
        path_cost = sum(weights[''.join(sorted([path[i], path[i + 1]]))] for i in range(len(path) - 1))
        for i in range(len(path) - 1):
            edge = ''.join(sorted([path[i], path[i + 1]]))
            pheromones[edge] += 1 / path_cost

    # Print updated pheromones
    print(f"Pheromone levels after decay and update: {pheromones}")

