from sys import stdin

def dfs(x, y):
    if x < 0 or x>= r or y < 0 or y >= c:
        return False
    if _map[x][y] == 0:
        _map[x][y] = 1
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        return True
    else:
        return False

r, c = map(int, stdin.readline().split())

_map = []
for _ in range(r):
    _map.append(list(map(int, stdin.readline().rstrip())))

res = 0
for i in range(r):
    for j in range(c):
        if dfs(i, j):
            res += 1

print(res)
    
