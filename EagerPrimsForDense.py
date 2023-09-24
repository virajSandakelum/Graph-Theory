import random
import matplotlib.pyplot as plt
import math
from EagerPrimsList import EagerPrimsList, run_eager_prims_list
from EagerPrimsMatrix import EagerPrimsMatrix, run_eager_prims_matrix


vertices = 5000
num_edges_list = [1000**2, 2000**2, 3000**2, 4000**2, 5000**2]

runtimes_list = []
runtimes_matrix = []

common_vertices = list(range(vertices))

nodes = list(map(str, range(5000)))

for num_edges in num_edges_list:
    print("\n")
    random_edges = [(random.randint(0, 4999), random.randint(0, 4999), random.randint(1, 100)) for _ in range(num_edges)]
    
    runtime_lazy_prims = run_eager_prims_list(nodes, random_edges)
    runtimes_list.append(runtime_lazy_prims)
    print(f"Runtime for Eager Prim's Algorithm with lists (V={vertices}, E={num_edges}): {runtime_lazy_prims:.6f} seconds")

    runtime_lazy_prims = run_eager_prims_matrix(nodes, random_edges)
    runtimes_matrix.append(runtime_lazy_prims)
    print(f"Runtime for Eager Prim's Algorithm with matrices (V={vertices}, E={num_edges}): {runtime_lazy_prims:.6f} seconds")
    

plt.plot(num_edges_list, runtimes_list, marker='o', linestyle='-', label="Eager Prim's Algorithm with Lists")
plt.plot(num_edges_list, runtimes_matrix, marker='o', linestyle='-', label="Eager Prim's Algorithm with Matrices")
plt.xlabel("Number of Edges")
plt.ylabel("Prim's Algorithm Runtime (seconds) vs. Number of Edges (Dense Graph)")
plt.legend()
plt.grid(True)
plt.show()


