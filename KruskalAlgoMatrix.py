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


def run_kruskal_matrix(nodes,all_edges):

    adj_matrix = KruskalAlgoMatrix(len(nodes), False)

    for source, destination, weight in all_edges:
        adj_matrix.add_edge(source, destination, weight)

    start_time = time.time()
    adj_matrix.findKruskal()
    end_time = time.time()
    
    runtime = end_time - start_time
    # print(f"Minimum Spanning Tree Value Adjacency Matrix: {adj_matrix.minimumSpanningTreeValue}")
    
    return runtime


