class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = set()

    def add_edge(self, u, v):
        if (v, u) not in self.edges: self.edges.add((u, v))

    def vertex_cover_approx(self):
        edge_pool = self.edges.copy()
        cover = set()
        while edge_pool:
            u, v = edge_pool.pop()
            cover.add(u)
            cover.add(v)
            edge_pool = {e for e in edge_pool if u not in e and v not in e}
        return cover


g = Graph([i for i in range(1, 6)])
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 5)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(4, 1)
g.add_edge(4, 5)
print(g.vertex_cover_approx())

