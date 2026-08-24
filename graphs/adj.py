
# Number of vertices
n = 4

# Create adjacency list
graph = [[] for _ in range(n)]

# Add edges
graph[0].append(1)
graph[1].append(0)

graph[0].append(2)
graph[2].append(0)

graph[1].append(3)
graph[3].append(1)

graph[2].append(3)
graph[3].append(2)

# Print adjacency list
for i in range(n):
    print(i, "->", graph[i])