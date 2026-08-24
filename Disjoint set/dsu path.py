class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


# Create DSU
dsu = DSU(5)

# Manually create a chain:
# 4 -> 3 -> 2 -> 1 -> 0
dsu.parent[1] = 0
dsu.parent[2] = 1
dsu.parent[3] = 2
dsu.parent[4] = 3

print("Parent before find:", dsu.parent)

# Find root of 4
print("Root of 4:", dsu.find(4))

print("Parent after find:", dsu.parent)