from sys import stdin
#from collections import deque

dx = [-1,  0,  1,  0]
dy = [ 0, -1,  0,  1]

def bfs(x, y):
    que = []
    que.append((x, y))
    while que:
        x, y = que.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c or _map[nx][ny] == 0:
                continue
            if _map[nx][ny] == 1:
                _map[nx][ny] = _map[x][y] + 1
                que.append((nx, ny))
    return _map[r-1][c-1]
r, c = map(int, stdin.readline().split())
_map = []
for _ in range(r):
    _map.append(list(map(int, stdin.readline().rstrip())))

print(bfs(0, 0))
