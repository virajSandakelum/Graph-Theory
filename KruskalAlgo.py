from queue import PriorityQueue


class KruskalAlgo:
    def __init__(self, nodes):
        self.Nodes = nodes
        self.adj_list = {}
        self.all_edges = []
        self.parent = {}
        self.minimumSpanningTreeValue = 0

        for node in self.Nodes:
            self.adj_list[node] = []

    def add_edge(self, u, v, weight):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        self.all_edges.append((u, v, weight))

    def initiateParent(self, v):
        self.parent[v] = v

    def findParent(self, v):
        if self.parent[v] == v:
            return v
        return self.findParent(self.parent[v])

    def union(self, u, v):
        self.parent[self.findParent(u)] = self.findParent(v)

    def print_adj_list(self):
        for node in self.Nodes:
            print(node, "->", self.adj_list[node])

    def findKruskal(self):
        for node in self.Nodes:
            self.parent[node] = node

        minimumSpanningTree = set()
        prioritizedEdges = PriorityQueue()

        for edge in self.all_edges:
            prioritizedEdges.put((edge[2], edge[0], edge[1]))

        while not prioritizedEdges.empty():
            weight, u, v = prioritizedEdges.get()

            if self.findParent(u) != self.findParent(v):
                minimumSpanningTree.add(u)
                minimumSpanningTree.add(v)
                self.minimumSpanningTreeValue += weight
                print(f"Edge: {u}-{v}, Weight: {weight}")
                print(f"Minimum Spanning Tree Value: {self.minimumSpanningTreeValue}")
                self.union(u, v)
            else:
                # This edge would create a cycle, so we don't add it.
                pass

        return minimumSpanningTree


nodes = ["A", "B", "C", "D", "E", "F", "G"]
graph = KruskalAlgo(nodes)

graph.add_edge("A", "D", 4)
graph.add_edge("A", "B", 2)
graph.add_edge("B", "F", 5)
graph.add_edge("D", "B", 1)
graph.add_edge("F", "B", 8)
graph.add_edge("D", "E", 2)
graph.add_edge("E", "B", 3)
graph.add_edge("F", "G", 1)
graph.add_edge("B", "G", 4)
graph.add_edge("G", "C", 6)
graph.add_edge("B", "C", 7)
graph.add_edge("E", "C", 10)

minimumSpanningTree = graph.findKruskal()

print(minimumSpanningTree)