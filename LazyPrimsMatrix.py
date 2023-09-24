import heapq
import time

class LazyPrimsMatrix:
    def __init__(self, num_vertices, is_directed):
        self.num_vertices = num_vertices
        self.is_directed = is_directed
        self.minimumSpanningTreeValue = 0
        self.nodeVisitingTrackingArray = {node: False for node in range(num_vertices)}
        self.adj_matrix = [[float('inf')] * num_vertices for _ in range(num_vertices)]
        self.MST = []

    def add_edge(self, source, destination, weight=1):
        self.adj_matrix[source][destination] = weight
        if not self.is_directed:
            self.adj_matrix[destination][source] = weight

    def findMST(self):
        visited = [False] * self.num_vertices
        priority_queue = []

        start_vertex = 0
        self.nodeVisitingTrackingArray[start_vertex] = True

        for v in range(self.num_vertices):
            if self.adj_matrix[start_vertex][v] != float('inf'):
                heapq.heappush(priority_queue, (self.adj_matrix[start_vertex][v], start_vertex, v))

        while priority_queue:
            weight, u, v = heapq.heappop(priority_queue)

            if self.nodeVisitingTrackingArray[u] and self.nodeVisitingTrackingArray[v]:
                continue

            self.minimumSpanningTreeValue += weight
            self.nodeVisitingTrackingArray[u] = True
            self.nodeVisitingTrackingArray[v] = True
            self.MST.append((u, v, weight))  # Add this edge to MST

            for neighbor in range(self.num_vertices):
                if (
                    self.adj_matrix[v][neighbor] != float('inf')
                    and not self.nodeVisitingTrackingArray[neighbor]
                ):
                    heapq.heappush(priority_queue, (self.adj_matrix[v][neighbor], v, neighbor))

    def print_adj_matrix(self):
        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print(row)

    def print_MST(self):
        start_time = time.time()
        self.findMST()
        end_time = time.time()

        print("\nMinimum Spanning Tree")
        for u, v, weight in self.MST:
            print(f"Edge: {u} - {v}, Weight: {weight}")

        print(f"\nMinimum Spanning Tree Value: {self.minimumSpanningTreeValue}")
        print(f"Runtime: {end_time - start_time:.6f} seconds")
        

def run_lazy_prims_matrix(nodes,all_edges):
    lazyMST = LazyPrimsMatrix(len(nodes), False)

    for u, v, weight in all_edges:
        lazyMST.add_edge(int(u), int(v), weight)
        
    start_time = time.time()
    lazyMST.findMST()
    end_time = time.time()

    return end_time - start_time

