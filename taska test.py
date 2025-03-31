import math

# Input n and k
n, k = map(int, input().split())

# Input coordinates
station = []
for _ in range(n):
    x, y = map(int, input().split())
    station.append((x, y))

# Calculate all pairwise distances
edges = []
for i in range(n):
    for j in range(i+1, n):
        dx = station[i][0] - station[j][0]
        dy = station[i][1] - station[j][1]
        distance = math.sqrt(dx*dx + dy*dy)
        edges.append((distance, i, j))

# Sort edges by distance
edges.sort()

# Kruskal's algorithm to find MST
parent = [i for i in range(n)]

def find(x):  # Changed from 'u' to 'x'
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

mst_edges = []
for edge in edges:
    d, u, v = edge
    u_root = find(u)  # These calls remain the same
    v_root = find(v)  # These calls remain the same
    if (u_root != v_root):
        parent[v_root] = u_root
        mst_edges.append(d)
        if len(mst_edges) == n-1:
            break
print(mst_edges)        