import heapq
import time

class LazyPrimsList:
    def __init__(self, nodes):
        self.Nodes = nodes
        self.adj_list = {}
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

        priority_queue = []

        for to_node, cost in self.adj_list[start_node]:
            heapq.heappush(priority_queue, (cost, start_node, to_node))

        while priority_queue:
            weight, u, v = heapq.heappop(priority_queue)

            if self.nodeVisitingTrackingArray[u] and self.nodeVisitingTrackingArray[v]:
                continue

            self.MST.append((u, v, weight))
            self.minimumSpanningTreeValue += weight

            if not self.nodeVisitingTrackingArray[u]:
                self.nodeVisitingTrackingArray[u] = True
                for neighbor, cost in self.adj_list[u]:
                    if not self.nodeVisitingTrackingArray[neighbor]:
                        heapq.heappush(priority_queue, (cost, u, neighbor))

            if not self.nodeVisitingTrackingArray[v]:
                self.nodeVisitingTrackingArray[v] = True
                for neighbor, cost in self.adj_list[v]:
                    if not self.nodeVisitingTrackingArray[neighbor]:
                        heapq.heappush(priority_queue, (cost, v, neighbor))

    def print_adj_list(self):
        print("\nGraph(adjacency list):")
        for node in self.Nodes:
            print(node, "->", self.adj_list[node])

        start_time = time.time()
        self.findMST()
        end_time = time.time()

        print("\nMinimum Spanning Tree")
        for u, v, weight in self.MST:
            print(f"Edge: {u} - {v}, Weight: {weight}")

        print(f"\nMinimum Spanning Tree Value: {self.minimumSpanningTreeValue}")
        print(f"Runtime: {end_time - start_time:.6f} seconds")


def run_lazy_prims_list(nodes, all_edges):
    lazyMST = LazyPrimsList(nodes)

    for u, v, weight in all_edges:
        lazyMST.add_edge(u, v, weight)

    start_time = time.time()
    lazyMST.findMST()
    end_time = time.time()

    return end_time - start_time

# nodes = ["0", "1", "2", "3", "4", "5", "6", "7"]
# all_edges = [
#     ("0", "1", 10),
#     ("0", "2", 1),
#     ("0", "3", 4),
#     ("1", "4", 0),
#     ("1", "2", 3),
#     ("2", "5", 8),
#     ("2", "3", 2),
#     ("3", "6", 7),
#     ("3", "5", 2),
#     ("4", "7", 8),
#     ("4", "5", 1),
#     ("5", "7", 9),
#     ("5", "6", 6),
#     ("6", "7", 12),
# ]

# lazyMST = LazyPrimsList(nodes)

# for u, v, weight in all_edges:
#     lazyMST.add_edge(u, v, weight)

# lazyMST.print_adj_list()
