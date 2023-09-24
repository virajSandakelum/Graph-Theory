import time
import random
import matplotlib.pyplot as plt

class KruskalAlgoMatrix:
    def __init__(self, num_vertices, is_directed):
        self.num_vertices = num_vertices
        self.is_directed = is_directed
        self.minimumSpanningTreeValue = 0
        self.adj_matrix = [[float('inf')] * num_vertices for _ in range(num_vertices)]
        self.parent = {}
        self.MST = []

    def add_edge(self, source, destination, weight=1):
        self.adj_matrix[source][destination] = weight
        if not self.is_directed:
            self.adj_matrix[destination][source] = weight

    def initiateParent(self, v):
        self.parent[v] = v

    def findParent(self, v):
        if self.parent[v] == v:
            return v
        return self.findParent(self.parent[v])

    def union(self, source, destination):
        self.parent[self.findParent(source)] = self.findParent(destination)

    def findKruskal(self):
        prioritizedEdges = []

        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.adj_matrix[i][j] != float('inf'):
                    prioritizedEdges.append((i, j, self.adj_matrix[i][j]))

        prioritizedEdges.sort(key=lambda x: x[2])

        for v in range(self.num_vertices):
            self.initiateParent(v)

        for edge in prioritizedEdges:
            source, destination, weight = edge

            if self.findParent(source) != self.findParent(destination):
                self.MST.append((source, destination, weight))
                self.union(source, destination)

        self.minimumSpanningTreeValue = sum(edge[2] for edge in self.MST)


def run_kruskal_matrix(num_vertices):
    random_edges = [(random.randint(0, num_vertices-1), random.randint(0, num_vertices-1), random.randint(1, 100)) for _ in range(num_vertices)]


    adj_matrix = KruskalAlgoMatrix(num_vertices, False)

    for source, destination, weight in random_edges:
        adj_matrix.add_edge(source, destination, weight)

    start_time = time.time()
    adj_matrix.findKruskal()
    end_time = time.time()
    
    runtime = end_time - start_time
    print(f"Minimum Spanning Tree Value: {adj_matrix.minimumSpanningTreeValue}")
    
    return runtime

# vertices = [1000, 2000, 3000, 4000, 5000]
# runtimes = []

# for num_vertices in vertices:
#     runtime = run_kruskal_matrix(num_vertices)
#     runtimes.append(runtime)
#     print(f"Runtime for {num_vertices} nodes: {runtime:.6f} seconds")

# plt.plot(vertices, runtimes, marker='o', linestyle='-')
# plt.title('Kruskal\'s Algorithm Runtime vs. Number of Vertices')
# plt.xlabel('Number of Vertices')
# plt.ylabel('Runtime (seconds)')
# plt.grid(True)
# plt.show()
