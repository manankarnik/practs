import numpy as np

def page_rank(am, d=0.85, tol=1e-6):
    n = am.shape[0]
    pr = np.ones(n)
    outlinks = am.sum(axis=1)

    while True:
        new_pr = np.zeros(n)
        for i in range(n):
            incoming_sum = sum([pr[j] / outlinks[j] for j in range(n) if adjacency_matrix[j, i] > 0])
            new_pr[i] = (1 - d) / n + d * incoming_sum
        if np.linalg.norm(new_pr - pr, 1) < tol:
            return new_pr
        pr = new_pr


nodes = ['A', 'B', 'C', 'D']
adjacency_matrix = np.array([
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
])
adjacency_matrix = np.array([
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 0]
])


pr = page_rank(adjacency_matrix)

for n, p in zip(nodes, pr):
    print(n, f"{p:.4f}")
