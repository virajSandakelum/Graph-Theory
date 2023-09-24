import heapq
import time

class IndexedPriorityQueue:
    def __init__(self):
        self.pq = []
        self.counter = 0
        self.index = {}

    def enqueue(self, node, cost):
        self.counter += 1
        entry = [cost, self.counter, node]
        self.index[node] = entry
        heapq.heappush(self.pq, entry)

    def dequeue(self):
        while self.pq:
            cost, counter, node = heapq.heappop(self.pq)
            if node in self.index:
                del self.index[node]
                return node, cost
        return None, None  

    def updatePQMinCost(self, node, new_cost):
        if node in self.index:
            cost, counter, _ = self.index[node]
            if new_cost < cost:
                self.index[node][0] = new_cost
                heapq.heapify(self.pq)

class EagerPrimsMatrix:
    def __init__(self, num_vertices, is_directed):
        self.num_vertices = num_vertices
        self.is_directed = is_directed
        self.MST = []
        self.minimumSpanningTreeValue = 0
        self.nodeVisitingTrackingArray = [False] * num_vertices
        self.adj_matrix = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, source, destination, weight=1):
        self.adj_matrix[source][destination] = weight
        if not self.is_directed:
            self.adj_matrix[destination][source] = weight

    def findMST(self):
        start_node = 0  
        priority_queue = IndexedPriorityQueue()
        for neighbor, weight in enumerate(self.adj_matrix[start_node]):
            if weight != float('inf'):
                priority_queue.enqueue(neighbor, weight)
        self.nodeVisitingTrackingArray[start_node] = True

        while len(self.MST) < self.num_vertices - 1:
            from_node, cost = priority_queue.dequeue()
            if from_node is None:
                break  

            if not self.nodeVisitingTrackingArray[from_node]:
                self.nodeVisitingTrackingArray[from_node] = True
                self.MST.append((from_node, cost))
                self.minimumSpanningTreeValue += cost

                for neighbor, weight in enumerate(self.adj_matrix[from_node]):
                    if weight != float('inf') and not self.nodeVisitingTrackingArray[neighbor]:
                        priority_queue.enqueue(neighbor, weight)

    def print_mst_edges(self):
        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print(row)      

        print("\nMinimum Spanning Tree:")
        for u, weight in self.MST:
            v = self.nodeVisitingTrackingArray.index(True)
            print(f"Edge: {u} - {v}, Weight: {weight}")

        print(f"\nMinimum Spanning Tree Value: {self.minimumSpanningTreeValue}")
        
        
def run_eager_prims_matrix(nodes, all_edges):
    eagerMST = EagerPrimsMatrix(len(nodes), False)

    for source, destination, weight in all_edges:
        eagerMST.add_edge(source, destination, weight)

    start_time = time.time()
    eagerMST.findMST()
    end_time = time.time()

    return end_time - start_time



# nodes = list(range(8)) 

# all_edges = [
#     (0, 1, 10),
#     (0, 2, 1),
#     (0, 3, 4),
#     (1, 4, 0),
#     (1, 2, 3),
#     (2, 5, 8),
#     (2, 3, 2),
#     (3, 6, 7),
#     (3, 5, 2),
#     (4, 7, 8),
#     (4, 5, 1),
#     (5, 7, 9),
#     (5, 6, 6),
#     (6, 7, 12),
# ]

# eagerMST = EagerPrimsMatrix(len(nodes), False)

# start_time = time.time()

# for source, destination, weight in all_edges:
#     eagerMST.add_edge(source, destination, weight)

# eagerMST.findMST()
# eagerMST.print_mst_edges()
# end_time = time.time()

# print(f"Runtime: {end_time - start_time:.6f} seconds")
