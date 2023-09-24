import heapq
from collections import defaultdict

class IndexedPriorityQueue:
    def __init__(self):
        self.pq = []  # Priority queue
        self.index = {}  # Mapping of items to their indices
        self.counter = 0  # Counter for maintaining the order of insertion
        
    


class EagerPrims:
    def __init__(self, nodes):
        self.Nodes = nodes
        self.adj_list = defaultdict(list)
        self.nodeVisitingTrackingArray = {node: False for node in self.Nodes}
        self.MST = []
        self.minimumSpanningTreeValue = 0

        for node in self.Nodes:
            self.adj_list[node] = []

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def findMST(self):
        start_node = self.Nodes[0]
        self.nodeVisitingTrackingArray[start_node] = True

        indexed_priority_queue = IndexedPriorityQueue()

        for to_node, cost in self.adj_list[start_node]:
            indexed_priority_queue.insert(to_node, cost)

        while not indexed_priority_queue.is_empty():
            u, u_priority = indexed_priority_queue.pop_min()

            if self.nodeVisitingTrackingArray[u]:
                continue

            self.MST.append((start_node, u, u_priority))
            self.minimumSpanningTreeValue += u_priority

            self.nodeVisitingTrackingArray[u] = True

            for v, v_priority in self.adj_list[u]:
                if not self.nodeVisitingTrackingArray[v]:
                    indexed_priority_queue.decrease_priority(v, v_priority)

    def print_adj_list(self):
        for node in self.Nodes:
            print(node, "->", self.adj_list[node])

        self.findMST()
        print("Minimum Spanning Tree:")
        for u, v, weight in self.MST:
            print(f"Edge: {u} - {v}, Weight: {weight}")
        
        print(f"Minimum Spanning Tree Value: {self.minimumSpanningTreeValue}")

# Define nodes and edges
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

# Create EagerPrims instance
eagerMST = EagerPrims(nodes)

# Add edges to the graph
for u, v, weight in all_edges:
    eagerMST.add_edge(u, v, weight)

# Print the adjacency list and MST
eagerMST.print_adj_list()
