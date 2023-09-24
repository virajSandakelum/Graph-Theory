import random
import matplotlib.pyplot as plt
from KruskalAlgoList import KruskalAlgoList, run_kruskal_list
from KruskalAlgoMatrix import KruskalAlgoMatrix, run_kruskal_matrix

vertices = 5000
num_edges_list = [1000**2, 2000**2, 3000**2, 4000**2, 5000**2]

runtimes_list = []
runtimes_matrix = []

common_vertices = list(range(vertices))

for num_edges in num_edges_list:
    print("\n")
    random_edges = [(random.choice(common_vertices), random.choice(common_vertices), random.randint(1, 100)) for _ in range(num_edges)]

    runtime_list = run_kruskal_list(vertices)
    runtimes_list.append(runtime_list)
    print(f"Runtime for Kruskal's Algorithm with lists (V={vertices}, E={num_edges}): {runtime_list:.6f} seconds")

    runtime_matrix = run_kruskal_matrix(vertices)
    runtimes_matrix.append(runtime_matrix)
    print(f"Runtime for Kruskal's Algorithm with matrices (V={vertices}, E={num_edges}): {runtime_matrix:.6f} seconds")


plt.plot(num_edges_list, runtimes_list, marker='o', linestyle='-', label="Kruskal's Algorithm with Lists")
plt.plot(num_edges_list, runtimes_matrix, marker='o', linestyle='-', label="Kruskal's Algorithm with Matrices")
plt.xlabel("Number of Edges")
plt.ylabel("Runtime (seconds)")
plt.title("Kruskal's Algorithm Runtime vs. Number of Edges(Sparse Graph)")
plt.legend()
plt.grid(True)
plt.show()
