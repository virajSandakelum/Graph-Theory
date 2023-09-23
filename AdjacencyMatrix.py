class AdjacencyMatrix:
    def __init__(self, num_vertices, is_directed):
        self.num_vertices = num_vertices
        self.is_directed = is_directed
        self.adj_matrix = [[0]*num_vertices for _ in range(num_vertices)]

    def add_edge(self, source, destination, weight=1):
        self.adj_matrix[source][destination] = weight
        if not self.is_directed:
            self.adj_matrix[destination][source] = weight

    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(row)



