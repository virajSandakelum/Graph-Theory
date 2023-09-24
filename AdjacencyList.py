class AdjacencyList:
    def __init__(self, nodes):
        self.Nodes = nodes
        self.adj_list = {}
        
        for node in self.Nodes:
            self.adj_list[node] = []
            
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_adj_list(self):
        print("\nAdjacency List")
        for node in self.Nodes:
            print(node,"->", self.adj_list[node])
                
                
nodes = ["A", "B", "C", "D", "E"]
graph = AdjacencyList(nodes)

all_edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),
    ("D", "E"),
]

for u, v in all_edges:
    graph.add_edge(u, v)

graph.print_adj_list()