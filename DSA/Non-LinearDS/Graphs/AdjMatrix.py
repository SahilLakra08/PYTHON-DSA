# Adjacency Matrix
# This program is giving the edges which are connected with each other.
# 1. Undirected Graph
vertex = [1,2,3,4]
AdjMatrix =[[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]
print('Adjacency Matrix : Undirected Graph')
for i in range(0,4):
    print('Vertex',i+1,':')
    for j in range(0,4):
        if AdjMatrix[i][j] == 1 :
            print(j+1,end="   ")
    print(' ')

# 2. Directed Graph

vertex = [1,2,3,4]
AdjMatrix =[[0,1,1,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]]
print('Adjacency Matrix : Directed Graph')
for i in range(0,4):
    print('Vertex',i+1,':')
    for j in range(0,4):
        if AdjMatrix[i][j] == 1 :
            print(j+1,end="   ")
    print(' ')

    # memory required = O(V*V)=space complexity
    
# Time complexity = Linked List takes more time because in Array we can directly go to
# i & j index without any traversal