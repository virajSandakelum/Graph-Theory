import random
import matplotlib.pyplot as plt
import math
from LazyPrimsList import LazyPrimsList, run_lazy_prims_list
from LazyPrimsMatrix import LazyPrimsMatrix, run_lazy_prims_matrix

vertices = 5000
num_edges_list = [1000, 2000, 3000, 4000, 5000]

runtimes_list = []
runtimes_matrix = []

common_vertices = list(range(vertices))

nodes = list(map(str, range(5000)))

for num_edges in num_edges_list:
    random_edges = [(str(random.randint(0, 4999)), str(random.randint(0, 4999)), random.randint(1, 100)) for _ in range(num_edges)]

    runtime_lazy_prims = run_lazy_prims_list(nodes, random_edges)
    runtimes_list.append(runtime_lazy_prims)
    print(f"Runtime for Lazy Prim's Algorithm with 5000 nodes and {num_edges} random edges: {runtime_lazy_prims:.6f} seconds")
    
for num_edges in num_edges_list:
    random_edges = [(random.randint(0, 4999), random.randint(0, 4999), random.randint(1, 100)) for _ in range(num_edges)]

    runtime_lazy_prims = run_lazy_prims_matrix(nodes, random_edges)
    runtimes_matrix.append(runtime_lazy_prims)
    print(f"Runtime for Lazy Prim's Algorithm with 5000 nodes and {num_edges} random edges: {runtime_lazy_prims:.6f} seconds")


plt.plot(num_edges_list, runtimes_list, label="List")
plt.plot(num_edges_list, runtimes_matrix, label="Matrix")
plt.xlabel("Number of Edges")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.show()
