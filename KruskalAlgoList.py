from queue import PriorityQueue
import time

class KruskalAlgoList:
    def __init__(self, nodes):
        self.Nodes = nodes
        self.adj_list = {}
        self.all_edges = []
        self.parent = {}
        self.minimumSpanningTreeValue = 0
        self.MST = []

        for node in self.Nodes:
            self.adj_list[node] = []

    def add_edge(self, source, destination, weight):
        self.adj_list[source].append(destination)
        self.adj_list[destination].append(source)
        self.all_edges.append((source, destination, weight))

    def initiateParent(self, node):
        self.parent[node] = node

    def findParent(self, node):
        if self.parent[node] == node:
            return node
        return self.findParent(self.parent[node])

    def union(self, source, destination):
        self.parent[self.findParent(source)] = self.findParent(destination)

    def findKruskal(self):
        for node in self.Nodes:
            self.initiateParent(node)

        minimumSpanningTree = set()
        prioritizedEdges = PriorityQueue()

        for edge in self.all_edges:
            prioritizedEdges.put((edge[2], edge[0], edge[1]))

        while not prioritizedEdges.empty():
            weight, source, destination = prioritizedEdges.get()

            if self.findParent(source) != self.findParent(destination):
                minimumSpanningTree.add((source, destination, weight))
                self.minimumSpanningTreeValue += weight
                self.union(source, destination)

        return minimumSpanningTree

    def printGraph(self):
        print("\nGraph(adjacency list):")
        for node in self.Nodes:
            print(f"{node} -> {self.adj_list[node]}")

# Define your nodes and edges here
nodes = ["0", "1", "2", "3", "4", "5", "6", "7"]
all_edges = [
    ("0", "1", 10),
    ("0", "2", 1),
    ("0", "3", 4),
    ("1", "4", 0),
    ("1", "2", 3),
    ("2", "5", 8),
    ("2", "3", 2),
    ("3", "6", 7),
    ("3", "5", 2),
    ("4", "7", 8),
    ("4", "5", 1),
    ("5", "7", 9),
    ("5", "6", 6),
    ("6", "7", 12),
]

graph = KruskalAlgoList(nodes)

start_time = time.time()

for source, destination, weight in all_edges:
    graph.add_edge(source, destination, weight)

minimumSpanningTree = graph.findKruskal()
graph.printGraph()

print("\nMinimum Spanning Tree")
for source, destination, weight in minimumSpanningTree:
    print(f"Edge: {source} - {destination}, Weight: {weight}")

print(f"\nMinimum Spanning Tree Value: {graph.minimumSpanningTreeValue}")

end_time = time.time()
runtime = end_time - start_time
print(f"Runtime: {runtime} seconds")
