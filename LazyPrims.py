import heapq

class LazyPrims:
    def __init__(self, nodes):
        self.Nodes = nodes
        self.adj_list = {}
        self.nodeVisitingTrackingArray = {node: False for node in self.Nodes}
        self.MST = []  
        
        for node in self.Nodes:
            self.adj_list[node] = []

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def findMST(self):
        start_node = self.Nodes[0]
        self.nodeVisitingTrackingArray[start_node] = True

        priority_queue = []

        for neighbor, weight in self.adj_list[start_node]:
            heapq.heappush(priority_queue, (weight, start_node, neighbor))
        
        print(priority_queue)
        

        # Main loop for Prim's algorithm
        while priority_queue:
            # Get the edge with the smallest weight
            weight, u, v = heapq.heappop(priority_queue)

            # If both endpoints are already in MST, skip this edge
            if self.nodeVisitingTrackingArray[u] and self.nodeVisitingTrackingArray[v]:
                continue

            # Add the edge to the MST
            self.MST.append((u, v, weight))

            # Mark the unvisited endpoint as visited
            if not self.nodeVisitingTrackingArray[u]:
                self.nodeVisitingTrackingArray[u] = True
                # Add edges from the newly visited node to the priority queue
                for neighbor, weight in self.adj_list[u]:
                    if not self.nodeVisitingTrackingArray[neighbor]:
                        heapq.heappush(priority_queue, (weight, u, neighbor))

            if not self.nodeVisitingTrackingArray[v]:
                self.nodeVisitingTrackingArray[v] = True
                # Add edges from the newly visited node to the priority queue
                for neighbor, weight in self.adj_list[v]:
                    if not self.nodeVisitingTrackingArray[neighbor]:
                        heapq.heappush(priority_queue, (weight, v, neighbor))

    def print_adj_list(self):
        for node in self.Nodes:
            print(node, "->", self.adj_list[node])

        self.findMST()
        print("Minimum Spanning Tree:")
        for u, v, weight in self.MST:
            print(f"Edge: {u} - {v}, Weight: {weight}")

nodes = ["0", "1", "2", "3", "4", "5", "6", "7"]
lazyMST = LazyPrims(nodes)

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

for u, v, weight in all_edges:
    lazyMST.add_edge(u, v, weight)

lazyMST.print_adj_list()
