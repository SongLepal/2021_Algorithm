from sys import stdin

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:   parent[b] = a
    else:   parent[a] = b

n, m = map(int, stdin.readline().split())
parent = [i for i in range(n)]
edges = []

for i in range(m):
    arr = list(map(int, stdin.readline().split()))
    a = arr[0] - 1
    b = arr[1] - 1
    c = arr[2]
    edges.append((c, a, b))
edges.sort()

result = 0
biggest = 0

for e in edges:
    c, a, b = e
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += c
        biggest = max(biggest, c)
print(result - biggest)


    
