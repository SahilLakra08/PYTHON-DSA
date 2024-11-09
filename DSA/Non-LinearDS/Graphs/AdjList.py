# # Adjacency List [Linked List]
# # also known as Array of pointers

# # 1. Undirected Graph

def addedge(adjlist, s, d):
    adjlist[s].append(d)
    adjlist[d].append(s)

vertices = 5
adjlist = [[] for _ in range(vertices)]

# Adding edges
addedge(adjlist, 1, 2)
addedge(adjlist, 1, 3)
addedge(adjlist, 1, 4)
addedge(adjlist, 2, 3)
addedge(adjlist, 3, 4)

# Print the adjacency list
for i in range(vertices):  # Should iterate over all vertices, including 0
    print(f"Vertex {i}: ", end="")
    for j in range(len(adjlist[i])):
        print(f"{adjlist[i][j]} -> ", end="")
    print("NULL")

# memory required = O(vertices+2Edges)
#space complexity = O(V+E)

# Time complexity = Linked List takes more time because in Array we can directly go to
# i & j index without any traversal