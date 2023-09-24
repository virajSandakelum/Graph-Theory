import heapq
from collections import defaultdict
import time

class IndexedPriorityQueue:
    def __init__(self):
        self.pq = []  
        self.counter = 0 
        self.index = {}
        self.from_node = []
        self.to_node = []
        self.cost = []

    def enqueue(self, from_node, to_node, cost):
        self.counter += 1
        entry = [cost, self.counter, from_node, to_node]
        self.index[(from_node, to_node)] = entry
        heapq.heappush(self.pq, entry)

    def dequeue(self):
        while self.pq:
            cost, counter, from_node, to_node = heapq.heappop(self.pq)
            if (from_node, to_node) in self.index:
                del self.index[(from_node, to_node)]
                return from_node, to_node, cost
        raise KeyError("Dequeue from an empty priority queue")

    def updatePQMinCost(self, from_node, to_node, new_cost):
        if (from_node, to_node) in self.index:
            cost, counter, _, _ = self.index[(from_node, to_node)]
            if new_cost < cost:
                self.index[(from_node, to_node)][0] = new_cost
                heapq.heapify(self.pq)


class EagerPrimsList:
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
        priority_queue = IndexedPriorityQueue()
        for neighbor, weight in self.adj_list[start_node]:
            priority_queue.enqueue(start_node, neighbor, weight)
        self.nodeVisitingTrackingArray[start_node] = True

        while priority_queue.pq:
            from_node, to_node, cost = priority_queue.dequeue()
            if not self.nodeVisitingTrackingArray[to_node]:
                self.nodeVisitingTrackingArray[to_node] = True
                self.MST.append((from_node, to_node, cost))
                self.minimumSpanningTreeValue += cost
                for neighbor, weight in self.adj_list[to_node]:
                    if not self.nodeVisitingTrackingArray[neighbor]:
                        priority_queue.enqueue(to_node, neighbor, weight)

    def print_adj_list(self):
        for node in self.Nodes:
            print(node, "->", self.adj_list[node])

        self.findMST()
        print("Minimum Spanning Tree:")
        for u, v, weight in self.MST:
            print(f"Edge: {u} - {v}, Weight: {weight}")

        print(f"Minimum Spanning Tree Value: {self.minimumSpanningTreeValue}")


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

eagerMST = EagerPrimsList(nodes)

start_time = time.time()
for u, v, weight in all_edges:
    eagerMST.add_edge(u, v, weight)

eagerMST.print_adj_list()
end_time = time.time()

print(f"Runtime: {end_time - start_time:.6f} seconds")
