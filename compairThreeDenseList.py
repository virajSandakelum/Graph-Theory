import random
import matplotlib.pyplot as plt
import math
from EagerPrimsList import EagerPrimsList, run_eager_prims_list
from LazyPrimsList import LazyPrimsList, run_lazy_prims_list
from KruskalAlgoList import KruskalAlgoList, run_kruskal_list

vertices = 5000
num_edges_list = [10000, 20000, 30000, 40000, 50000]

runtimes_lazy_prims = []
runtimes_eager_prims = []
runtimes_kruskal = []

common_vertices = list(range(vertices))

nodes = list(map(str, range(5000)))

for num_edges in num_edges_list:
    print("\n")
    random_edges = [(str(random.randint(0, 4999)), str(random.randint(0, 4999)), random.randint(1, 100)) for _ in range(num_edges)]

    runtime_lazy_prims = run_lazy_prims_list(nodes, random_edges)
    runtimes_lazy_prims.append(runtime_lazy_prims)
    print(f"Runtime for Lazy Prim's Algorithm with lists (V={vertices}, E={num_edges}): {runtime_lazy_prims:.6f} seconds")
    
    runtime_eager_prims = run_eager_prims_list(nodes, random_edges)
    runtimes_eager_prims.append(runtime_eager_prims)
    print(f"Runtime for Eager Prim's Algorithm with lists (V={vertices}, E={num_edges}): {runtime_eager_prims:.6f} seconds")
    
    runtime_kruskal = run_kruskal_list(nodes, random_edges)
    runtimes_kruskal.append(runtime_kruskal)
    print(f"Runtime for Kruskal's Algorithm with lists (V={vertices}, E={num_edges}): {runtime_kruskal:.6f} seconds")

plt.plot(num_edges_list, runtimes_lazy_prims, marker='o', linestyle='-', label="Lazy Prim's Algorithm with Lists")
plt.plot(num_edges_list, runtimes_eager_prims, marker='o', linestyle='-', label="Eager Prim's Algorithm with Lists")
plt.plot(num_edges_list, runtimes_kruskal, marker='o', linestyle='-', label="Kruskal's Algorithm with Lists")
plt.xlabel("Number of Edges")
plt.ylabel("Algorithm Runtime (seconds)")
plt.title("Algorithm Runtimes vs. Number of Edges (Dense Graph)")
plt.legend()
plt.grid(True)
plt.show()
