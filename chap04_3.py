from sys import stdin

r, c = map(int, stdin.readline().split())
x, y, d = map(int, stdin.readline().split())

_d = [[-1, 0], [0, 1], [1, 0], [0, -1]] #북0동1남2서3
_visit = [[0] * c for _ in range(r)] #0 = not-visited
_map = []
for _ in range(r):
    _map.append(list(map(int, stdin.readline().split())))
cnt = 0
turn = 0

while True:
    d -= 1 #turn left
    if d == -1:
        d = 3
    point = [x + _d[d][0], y + _d[d][1]]
    if ((_visit[point[0]][point[1]] == 0) and (_map[point[0]][point[1]] == 0)):
        _visit[point[0]][point[1]] = 1
        x = point[0]
        y = point[1]
        cnt += 1
        turn = 0
    else:
        turn += 1
    if turn == 4:
        point = [x - _d[d][0], y - _d[d][1]]
        if _map[point[0]][point[1]] == 0:
            x = point[0]
            y = point[1]
        else:
            break
        turn = 0
print(cnt)
