def tsp(mat):
    n = len(mat)
    tour = [0]
    visited = [False] * n
    visited[0] = True

    for _ in range(1, n):
        next = -1
        last = tour[-1]
        min_dist = float("inf")
        
        for i in range(n):
            if not visited[i] and mat[last][i] < min_dist:
                min_dist = mat[last][i]
                next = i

        visited[next] = True
        tour.append(next)

    return tour + [tour[0]]


mat = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(tsp(mat))
        

