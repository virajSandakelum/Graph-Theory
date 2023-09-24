from queue import PriorityQueue
import time
import random
import matplotlib.pyplot as plt

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
        self.adj_list[source].append((destination, weight))
        self.adj_list[destination].append((source, weight))
        self.all_edges.append((source, destination, weight))

    def initiateParent(self, node):
        self.parent[node] = node

    def findParent(self, node):
        while node != self.parent[node]:
            node = self.parent[node]
        return node

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


def run_kruskal_list(nodes, all_edges):
    adj_list = KruskalAlgoList(nodes)

    for source, destination, weight in all_edges:
        adj_list.add_edge(source, destination, weight)

    start_time = time.time()
    adj_list.findKruskal()
    end_time = time.time()

    runtime = end_time - start_time
    return runtime
