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

n, m = map(int, stdin.readline().split(' '))
parent = []
for i in range(n+1):
    parent.append(i)

for i in range(m):
    o, a, b = map(int, stdin.readline().split(' '))
    if not o:
        union(parent, a, b)
    else:
        if find(parent, a) == find(parent, b):
            print("Yes")
        else:
            print("No")
